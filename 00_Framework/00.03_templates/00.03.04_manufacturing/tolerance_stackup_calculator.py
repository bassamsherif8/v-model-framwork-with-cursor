"""
Tolerance Stack-Up Calculator
Calculates worst-case and statistical (RSS) tolerance stack-ups

This module calculates tolerance stack-ups for critical dimensions in assemblies,
using both worst-case and statistical (Root Sum Square) methods.

Usage:
    from tolerance_stackup_calculator import calculate_tolerance_stackup
    result = calculate_tolerance_stackup(tolerance_chain)
"""

import math
import os
import sys
from typing import List, Dict, Tuple

# Add manufacturing data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

try:
    from manufacturing_data import get_part_manufacturing_specs, get_all_part_numbers
except ImportError:
    def get_part_manufacturing_specs(part_number):
        return None
    def get_all_part_numbers():
        return []

class ToleranceChain:
    """
    Represents a tolerance chain (dimension stack) in an assembly
    """
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.components = []  # List of (dimension_name, nominal, tolerance, part_number)
    
    def add_component(self, dimension_name, nominal, tolerance, part_number, is_critical=False):
        """
        Add a component to the tolerance chain
        
        Args:
            dimension_name (str): Name of dimension
            nominal (float): Nominal dimension value (mm)
            tolerance (float): Tolerance value (±mm)
            part_number (str): Part number
            is_critical (bool): Whether this is a critical dimension
        """
        self.components.append({
            "dimension": dimension_name,
            "nominal": nominal,
            "tolerance": tolerance,
            "part": part_number,
            "critical": is_critical
        })
    
    def calculate_worst_case(self):
        """
        Calculate worst-case tolerance stack-up
        
        Returns:
            dict: Worst-case results
        """
        nominal_sum = sum(c["nominal"] for c in self.components)
        tolerance_sum = sum(c["tolerance"] for c in self.components)
        
        return {
            "nominal": nominal_sum,
            "tolerance": tolerance_sum,
            "min": nominal_sum - tolerance_sum,
            "max": nominal_sum + tolerance_sum,
            "range": 2 * tolerance_sum
        }
    
    def calculate_rss(self):
        """
        Calculate statistical (Root Sum Square) tolerance stack-up
        
        Returns:
            dict: RSS results
        """
        nominal_sum = sum(c["nominal"] for c in self.components)
        
        # RSS: sqrt(sum of squares of tolerances)
        tolerance_squared_sum = sum(c["tolerance"] ** 2 for c in self.components)
        tolerance_rss = math.sqrt(tolerance_squared_sum)
        
        return {
            "nominal": nominal_sum,
            "tolerance": tolerance_rss,
            "min": nominal_sum - tolerance_rss,
            "max": nominal_sum + tolerance_rss,
            "range": 2 * tolerance_rss
        }

def calculate_tolerance_stackup(tolerance_chain: ToleranceChain, requirement: float = None):
    """
    Calculate tolerance stack-up for a tolerance chain
    
    Args:
        tolerance_chain (ToleranceChain): Tolerance chain to analyze
        requirement (float): Required tolerance (optional, for validation)
        
    Returns:
        dict: Stack-up analysis results
    """
    worst_case = tolerance_chain.calculate_worst_case()
    rss = tolerance_chain.calculate_rss()
    
    results = {
        "chain_name": tolerance_chain.name,
        "description": tolerance_chain.description,
        "components": tolerance_chain.components,
        "worst_case": worst_case,
        "rss": rss,
        "requirement": requirement,
        "meets_requirement_wc": None,
        "meets_requirement_rss": None
    }
    
    if requirement is not None:
        results["meets_requirement_wc"] = worst_case["tolerance"] <= requirement
        results["meets_requirement_rss"] = rss["tolerance"] <= requirement
    
    return results

def analyze_critical_dimensions(part_numbers=None):
    """
    Analyze critical dimensions from manufacturing data
    
    Args:
        part_numbers (list): List of part numbers to analyze (optional)
        
    Returns:
        list: List of tolerance stack-up results
    """
    if part_numbers is None:
        part_numbers = get_all_part_numbers()
    
    results = []
    
    for part_number in part_numbers:
        specs = get_part_manufacturing_specs(part_number)
        if not specs:
            continue
        
        dimensions = specs.get("dimensions", {})
        
        for dim_name, dim_data in dimensions.items():
            if dim_data.get("is_critical", False):
                # Create tolerance chain for this critical dimension
                chain = ToleranceChain(
                    f"{part_number}_{dim_name}",
                    f"Critical dimension {dim_name} for {part_number}"
                )
                
                chain.add_component(
                    dim_name,
                    dim_data["value"],
                    dim_data["tolerance"],
                    part_number,
                    is_critical=True
                )
                
                # Calculate stack-up (single component for now)
                result = calculate_tolerance_stackup(chain)
                results.append(result)
    
    return results

def generate_tolerance_report(results, output_file=None):
    """
    Generate tolerance stack-up analysis report
    
    Args:
        results (list): List of tolerance stack-up results
        output_file (str): Output file path (optional)
    """
    if output_file is None:
        output_file = os.path.join(SCRIPT_DIR, "tolerance_stackup_report.md")
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    from datetime import datetime
    
    lines = [
        "# Tolerance Stack-Up Analysis Report",
        "",
        f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Summary",
        "",
        f"- **Total Chains Analyzed:** {len(results)}",
        "",
        "## Detailed Results",
        ""
    ]
    
    for result in results:
        lines.extend([
            f"### {result['chain_name']}",
            "",
            f"**Description:** {result['description']}",
            "",
            "**Components:**",
            "",
            "| Dimension | Nominal (mm) | Tolerance (±mm) | Part |",
            "|-----------|--------------|------------------|------|"
        ])
        
        for comp in result["components"]:
            lines.append(
                f"| {comp['dimension']} | {comp['nominal']:.3f} | "
                f"±{comp['tolerance']:.3f} | {comp['part']} |"
            )
        
        lines.extend([
            "",
            "**Worst-Case Analysis:**",
            f"- Nominal: {result['worst_case']['nominal']:.3f} mm",
            f"- Tolerance: ±{result['worst_case']['tolerance']:.3f} mm",
            f"- Range: {result['worst_case']['min']:.3f} to {result['worst_case']['max']:.3f} mm",
            "",
            "**Statistical (RSS) Analysis:**",
            f"- Nominal: {result['rss']['nominal']:.3f} mm",
            f"- Tolerance: ±{result['rss']['tolerance']:.3f} mm",
            f"- Range: {result['rss']['min']:.3f} to {result['rss']['max']:.3f} mm",
            ""
        ])
        
        if result["requirement"] is not None:
            wc_status = "✅ PASS" if result["meets_requirement_wc"] else "❌ FAIL"
            rss_status = "✅ PASS" if result["meets_requirement_rss"] else "❌ FAIL"
            
            lines.extend([
                f"**Requirement:** ±{result['requirement']:.3f} mm",
                f"- Worst-Case: {wc_status}",
                f"- RSS: {rss_status}",
                ""
            ])
        
        lines.append("---")
        lines.append("")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    print(f"Tolerance stack-up report saved to: {output_file}")

if __name__ == "__main__":
    print("Tolerance Stack-Up Calculator")
    print("="*60)
    print()
    
    # Example: Analyze critical dimensions
    print("Analyzing critical dimensions...")
    results = analyze_critical_dimensions()
    
    if results:
        print(f"Found {len(results)} critical dimensions to analyze")
        
        # Generate report
        generate_tolerance_report(results)
        
        # Summary
        print()
        print("="*60)
        print("TOLERANCE STACK-UP SUMMARY")
        print("="*60)
        
        for result in results:
            print(f"\n{result['chain_name']}:")
            print(f"  Worst-Case: ±{result['worst_case']['tolerance']:.3f} mm")
            print(f"  RSS: ±{result['rss']['tolerance']:.3f} mm")
            
            if result["requirement"]:
                wc_ok = result["meets_requirement_wc"]
                rss_ok = result["meets_requirement_rss"]
                print(f"  Requirement: ±{result['requirement']:.3f} mm")
                print(f"    Worst-Case: {'✅ PASS' if wc_ok else '❌ FAIL'}")
                print(f"    RSS: {'✅ PASS' if rss_ok else '❌ FAIL'}")
    else:
        print("No critical dimensions found in manufacturing data")

