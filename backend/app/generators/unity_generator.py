"""
Unity project generator
Creates C# scripts and project structure based on game idea and enhancements
"""

import os
import json
import zipfile
import tempfile
from typing import Dict, List, Any
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import uuid

class UnityGenerator:
    def __init__(self):
        """Initialize the Unity generator with templates"""
        self.templates_dir = Path(__file__).parent.parent / "templates"
        self.env = Environment(loader=FileSystemLoader(str(self.templates_dir)))
        
        # Define script templates
        self.script_templates = {
            "PlayerController": "PlayerController.cs.j2",
            "GameManager": "GameManager.cs.j2", 
            "Collectible": "Collectible.cs.j2",
            "EnemyAI": "EnemyAI.cs.j2",
            "LevelManager": "LevelManager.cs.j2",
            "UIManager": "UIManager.cs.j2"
        }
    
    async def generate_project(self, game_idea: str, selected_enhancements: Dict[str, List[str]]) -> Dict[str, Any]:
        """
        Generate a complete Unity project based on game idea and enhancements
        
        Args:
            game_idea: Original game description
            selected_enhancements: Dictionary of category -> selected suggestions
            
        Returns:
            Dictionary with project info including download URL
        """
        
        # Create temporary directory for project
        with tempfile.TemporaryDirectory() as temp_dir:
            project_path = Path(temp_dir) / "unity_project"
            project_path.mkdir()
            
            # Generate project structure
            self._create_project_structure(project_path)
            
            # Generate C# scripts
            scripts = self._generate_scripts(game_idea, selected_enhancements, project_path)
            
            # Generate project files
            self._generate_project_files(project_path, game_idea)
            
            # Create zip file
            zip_path = self._create_project_zip(project_path, game_idea)
            
            # For now, return basic info (in real app, upload to cloud storage)
            return {
                "download_url": f"/downloads/{os.path.basename(zip_path)}",
                "file_count": len(list(project_path.rglob("*"))),
                "main_scripts": [script["name"] for script in scripts],
                "project_path": str(zip_path)
            }
    
    def _create_project_structure(self, project_path: Path):
        """Create basic Unity project folder structure"""
        
        # Create standard Unity folders
        folders = [
            "Assets",
            "Assets/Scripts",
            "Assets/Scripts/Player",
            "Assets/Scripts/Enemies", 
            "Assets/Scripts/Managers",
            "Assets/Scripts/UI",
            "Assets/Scripts/Collectibles",
            "Assets/Prefabs",
            "Assets/Scenes",
            "Assets/Materials",
            "Assets/Textures",
            "ProjectSettings"
        ]
        
        for folder in folders:
            (project_path / folder).mkdir(parents=True, exist_ok=True)
    
    def _generate_scripts(self, game_idea: str, selected_enhancements: Dict[str, List[str]], project_path: Path) -> List[Dict]:
        """Generate C# scripts based on game idea and enhancements"""
        
        scripts = []
        scripts_dir = project_path / "Assets" / "Scripts"
        
        # Always generate core scripts
        core_scripts = [
            ("PlayerController", "Player"),
            ("GameManager", "Managers"),
            ("UIManager", "UI")
        ]
        
        for script_name, folder in core_scripts:
            script_content = self._generate_script_content(
                script_name, game_idea, selected_enhancements
            )
            
            script_path = scripts_dir / folder / f"{script_name}.cs"
            script_path.parent.mkdir(exist_ok=True)
            
            with open(script_path, 'w') as f:
                f.write(script_content)
            
            scripts.append({
                "name": script_name,
                "path": str(script_path.relative_to(project_path)),
                "content": script_content
            })
        
        # Generate optional scripts based on enhancements
        if "Collectible items" in selected_enhancements.get("mechanics", []):
            collectible_script = self._generate_script_content("Collectible", game_idea, selected_enhancements)
            collectible_path = scripts_dir / "Collectibles" / "Collectible.cs"
            with open(collectible_path, 'w') as f:
                f.write(collectible_script)
            scripts.append({
                "name": "Collectible",
                "path": str(collectible_path.relative_to(project_path)),
                "content": collectible_script
            })
        
        if any("enemy" in enhancement.lower() for enhancement in selected_enhancements.get("mechanics", [])):
            enemy_script = self._generate_script_content("EnemyAI", game_idea, selected_enhancements)
            enemy_path = scripts_dir / "Enemies" / "EnemyAI.cs"
            with open(enemy_path, 'w') as f:
                f.write(enemy_script)
            scripts.append({
                "name": "EnemyAI", 
                "path": str(enemy_path.relative_to(project_path)),
                "content": enemy_script
            })
        
        if "Multiple levels" in selected_enhancements.get("levels", []):
            level_script = self._generate_script_content("LevelManager", game_idea, selected_enhancements)
            level_path = scripts_dir / "Managers" / "LevelManager.cs"
            with open(level_path, 'w') as f:
                f.write(level_script)
            scripts.append({
                "name": "LevelManager",
                "path": str(level_path.relative_to(project_path)), 
                "content": level_script
            })
        
        return scripts
    
    def _generate_script_content(self, script_name: str, game_idea: str, selected_enhancements: Dict[str, List[str]]) -> str:
        """Generate C# script content using Jinja2 templates"""
        
        # Get template
        template_name = self.script_templates.get(script_name, f"{script_name}.cs.j2")
        
        try:
            template = self.env.get_template(template_name)
        except:
            # Fallback to basic template
            template = self.env.get_template("BasicScript.cs.j2")
        
        # Prepare template variables
        template_vars = {
            "game_idea": game_idea,
            "enhancements": selected_enhancements,
            "script_name": script_name,
            "has_double_jump": "Double jump" in selected_enhancements.get("mechanics", []),
            "has_collectibles": "Collectible" in selected_enhancements.get("mechanics", []),
            "has_enemies": any("enemy" in e.lower() for e in selected_enhancements.get("mechanics", [])),
            "has_multiple_levels": "Multiple levels" in selected_enhancements.get("levels", [])
        }
        
        return template.render(**template_vars)
    
    def _generate_project_files(self, project_path: Path, game_idea: str):
        """Generate Unity project configuration files"""
        
        # Generate README
        readme_content = f"""# {game_idea}

This Unity project was generated by AI Unity Game Generator.

## Getting Started

1. Open Unity 2020.3 or later
2. Open this project folder
3. Open the Main scene in Assets/Scenes/
4. Press Play to test the game

## Generated Scripts

- PlayerController.cs: Handles player movement and input
- GameManager.cs: Manages game state and flow
- UIManager.cs: Handles UI elements

## Customization

Feel free to modify the generated scripts to match your vision!
"""
        
        with open(project_path / "README.md", 'w') as f:
            f.write(readme_content)
        
        # Generate basic scene file (simplified)
        scene_content = """%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!29 &1
OcclusionCullingSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 2
  m_OcclusionBakeSettings:
    smallestOccluder: 5
    smallestHole: 0.25
    backfaceThreshold: 100
  m_SceneGUID: 00000000000000000000000000000000
  m_OcclusionCullingData: {fileID: 0}
--- !u!104 &2
RenderSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 9
  m_Fog: 0
  m_FogColor: {r: 0.5, g: 0.5, b: 0.5, a: 1}
  m_FogMode: 3
  m_FogDensity: 0.01
  m_LinearFogStart: 0
  m_LinearFogEnd: 300
  m_AmbientMode: 0
  m_AmbientSkyColor: {r: 0.212, g: 0.227, b: 0.259, a: 1}
  m_AmbientEquatorColor: {r: 0.114, g: 0.125, b: 0.133, a: 1}
  m_AmbientGroundColor: {r: 0.047, g: 0.043, b: 0.035, a: 1}
  m_AmbientIntensity: 1
  m_AmbientMode: 3
  m_SubtractiveShadowColor: {r: 0.42, g: 0.478, b: 0.627, a: 1}
  m_SkyboxMaterial: {fileID: 0}
  m_HaloStrength: 0.5
  m_FlareStrength: 1
  m_FlareFadeSpeed: 3
  m_HaloTexture: {fileID: 0}
  m_SpotCookie: {fileID: 10001, guid: 0000000000000000e000000000000000, type: 0}
  m_DefaultReflectionMode: 0
  m_DefaultReflectionResolution: 128
  m_ReflectionBounces: 1
  m_ReflectionIntensity: 1
  m_CustomReflection: {fileID: 0}
  m_Sun: {fileID: 0}
  m_IndirectSpecularColor: {r: 0, g: 0, b: 0, a: 1}
  m_UseRadianceAmbientProbe: 0
"""
        
        with open(project_path / "Assets" / "Scenes" / "Main.unity", 'w') as f:
            f.write(scene_content)
    
    def _create_project_zip(self, project_path: Path, game_idea: str) -> str:
        """Create a zip file of the Unity project"""
        
        # Create a safe filename from game idea
        safe_name = "".join(c for c in game_idea if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_name = safe_name.replace(' ', '_')[:50]  # Limit length
        
        zip_filename = f"unity_project_{safe_name}_{uuid.uuid4().hex[:8]}.zip"
        zip_path = project_path.parent / zip_filename
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in project_path.rglob('*'):
                if file_path.is_file():
                    arcname = file_path.relative_to(project_path)
                    zipf.write(file_path, arcname)
        
        return str(zip_path) 