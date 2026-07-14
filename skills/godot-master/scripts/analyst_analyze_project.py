import os
import re
import json
from datetime import datetime

# Anara Insight Protocol: Godot 4.6+ Scoring Calibration
# Focused on Architecture (Decoupling), Modernity (4.6 APIs), and Scalability.

class AnaraAnalyst:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.stats = {
            "files_scanned": 0,
            "architecture_score": 0,
            "modernity_score": 0,
            "performance_score": 0,
            "total_score": 0,
            "metrics": {
                "typed_containers": 0,
                "modern_signals": 0,
                "decoupled_ui": 0,
                "worker_threads": 0,
                "avg_complexity": 0,
                "godot_4_6_features": 0
            }
        }

    def analyze(self):
        print(f"✨ Anara Insight Protocol Initiated for: {self.root_dir}")
        for root, dirs, files in os.walk(self.root_dir):
            if ".git" in dirs: dirs.remove(".git")
            
            for file in files:
                if file.endswith(".gd"):
                    self.stats["files_scanned"] += 1
                    file_path = os.path.join(root, file)
                    self._analyze_file(file_path)
        
        self._calculate_final_scores()
        self._generate_results()

    def _analyze_file(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # 1. Architecture: Decoupling (Signals vs Direct Parent Hunting)
                signals = len(re.findall(r'signal\s+\w+', content))
                parent_hunts = len(re.findall(r'get_parent\(\)', content))
                self.stats["metrics"]["modern_signals"] += signals
                self.stats["metrics"]["decoupled_ui"] += 1 if "signal_bus" in content.lower() or "%" in content else 0
                
                # 2. Modernity: Typed Containers & 4.6 APIs
                typed_containers = len(re.findall(r'(Array|Dictionary)\[', content))
                worker_threads = len(re.findall(r'WorkerThreadPool', content))
                callables = len(re.findall(r'\.bind\(', content))
                
                self.stats["metrics"]["typed_containers"] += typed_containers
                self.stats["metrics"]["worker_threads"] += worker_threads
                self.stats["metrics"]["godot_4_6_features"] += (worker_threads + callables)
                
                # 3. Performance: Main Thread health
                # (Simple proxy: ratio of complex logic inside _process)
                process_logic = len(re.findall(r'func\s+_process.*?\{.*?\}', content, re.DOTALL))
                # (Ideally we'd calculate complexity here)
                
        except Exception as e:
            print(f"Error analyzing {path}: {e}")

    def _calculate_final_scores(self):
        # Weighted Scoring (Anara Protocol)
        count = max(1, self.stats["files_scanned"])
        
        # Architecture Score (40%)
        # Based on Decoupling Ratio (Signals / ParentHunts)
        arch_base = min(100, (self.stats["metrics"]["modern_signals"] * 10) + (self.stats["metrics"]["decoupled_ui"] * 20))
        self.stats["architecture_score"] = int(arch_base)
        
        # Modernity Score (30%)
        # Based on Typed Container penetration and 4.6 Feature usage
        mod_base = min(100, (self.stats["metrics"]["typed_containers"] * 5) + (self.stats["metrics"]["godot_4_6_features"] * 10))
        self.stats["modern_score"] = int(mod_base)
        
        # Performance Score (30%)
        # Based on Threading utilization and Resource efficiency (simple coefficient)
        perf_base = min(100, 60 + (self.stats["metrics"]["worker_threads"] * 15))
        self.stats["performance_score"] = int(perf_base)
        
        # Grand Total
        self.stats["total_score"] = int(
            (self.stats["architecture_score"] * 0.4) +
            (self.stats["modern_score"] * 0.3) +
            (self.stats["performance_score"] * 0.3)
        )

    def _generate_results(self):
        results_path = os.path.join(self.root_dir, "analysis_results.json")
        with open(results_path, 'w', encoding='utf-8') as f:
            json.dump(self.stats, f, indent=4)
        print(f"✨ Analysis Complete. Results written to: {results_path}")

if __name__ == "__main__":
    target = os.getcwd()
    analyst = AnaraAnalyst(target)
    analyst.analyze()
