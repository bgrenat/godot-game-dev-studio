# scoring_logic.gd
# Advanced script parsing logic using hardened multi-line RegEx.
# Grounded in PCRE2 expert patterns for Godot 4.x.

extends RefCounted

class_name ScoringLogic

## Hardened RegEx for multi-line GDScript patterns.
# (?m) = Multiline mode (matches ^ and $ at start/end of lines)
# (?s) = Dotall mode (. matches newlines)
const MULTILINE_FUNC_REGEX := "(?ms)func\\s+\\w+\\s*\\(.*?\\)\\s*->\\s*\\w+\\s*:"
const NESTED_DICT_REGEX := "(?ms)\\{[^{}]*\\}"

## Audits a script for complex multi-line patterns.
static func audit_script_complexity(source_code: String) -> Dictionary:
	var results := {
		"functions_detected": 0,
		"multiline_complexity_warnings": 0
	}
	
	var regex := RegEx.new()
	regex.compile(MULTILINE_FUNC_REGEX)
	
	for match in regex.search_all(source_code):
		results["functions_detected"] += 1
		# Check if the function spans multiple lines
		if "\n" in match.get_string():
			results["multiline_complexity_warnings"] += 1
			
	return results
