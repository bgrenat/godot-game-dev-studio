class_name WebLocalStorageWrapper
extends Node

## Expert wrapper for browser localStorage.
## Features JSON serialization, error handling, and quota checks.

func save_data(key: String, value: Variant) -> bool:
	if not OS.has_feature("web"): return false

	var json_str := JSON.stringify(value)
	var storage := JavaScriptBridge.get_interface("localStorage")

	# GDScript has no try/except: let JavaScript catch QuotaExceededError and report back.
	var ok: Variant = JavaScriptBridge.eval(
		"(function(k, v){ try { localStorage.setItem(k, v); return true; } catch (e) { return false; } })(%s, %s)"
		% [JSON.stringify(key), JSON.stringify(json_str)])
	if not ok:
		push_error("WebLocalStorage: Storage quota exceeded or blocked.")
		return false
	return true

func load_data(key: String) -> Variant:
	var storage := JavaScriptBridge.get_interface("localStorage")
	var data = storage.getItem(key)
	if data:
		return JSON.parse_string(data)
	return null

## Rule: Browsers may wipe localStorage; never use it for mission-critical core data.
