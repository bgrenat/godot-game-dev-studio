extends Node
## Editor tool to programmatically iterate and export all defined presets in one click.

func export_all() -> void:
    var config := ConfigFile.new()
    var err = config.load("res://export_presets.cfg")
    if err != OK:
        push_error("Failed to load export_presets.cfg")
        return
        
    for section in config.get_sections():
        if section.begins_with("preset."):
            var preset_name = config.get_value(section, "name")
            var path = config.get_value(section, "export_path")
            
            print("Exporting preset: ", preset_name, " to ", path)
            
            # Execute Godot headless for export
            var output = []
            var exit_code = OS.execute(OS.get_executable_path(), ["--headless", "--export-release", preset_name, path], output)
            
            if exit_code == 0:
                print("Successfully exported ", preset_name)
            else:
                push_error("Failed to export ", preset_name, ". Exit code: ", exit_code)
