# V-REP-Blender-Tools

Currently this repo contains two files that work together. 

The first file is a V-REP model (BlenderExporter.ttm). This model records the V-REP poses of all visible meshes from the simulation start, and exports them when the simulation stops in a text file (it also exports the visible meshas as a .obj file).

The second file is a python script that can be used in blender. This python script reads all the .obj files writtern by BlenderExporter.ttm into Blender. The poses are converted to keyframes in blender.

An example created by this tool: https://youtu.be/5H-j-KT4A1M

# Instructions

Youtube video with instructions: https://youtu.be/aevqp5xcfTQ 

- Import BlenderExporter.ttm in any V-REP Scene
- Run the simulation for the time that is needed
- Stop the simulation
- This is all in V-REP, go to blender 2.8 now.

- Create a new script in blender (https://www.youtube.com/watch?v=rHzf3Dku_cE&t=207s)
- Paste the contents of copyInBlender.py in this script an run it.
- The objects and animations work in blender now, so this is it.  

# Modifications

I want to change the folder in which intermediate files are stored. Well this is easy, change line 6 of copyInBlender.py, and line 5 of the child script of BlenderExporter.ttm.

I do not like that the animation starts recording when the simulation starts. Well you cou easily change this. Time steps are recorded through following code (in BlenderExporter.ttm's child script):
function sysCall_actuation()
    -- Do with this what you want
    recordPose()
end

Just call recordPose() when you like it.

I do not want to export ALL visible meshes. Well, it is actually easy to modify which meshes are exported. The meshes that are exported are selected by the following code:
getVisibleHandles = function()
	handles = sim.getObjectsInTree(sim.handle_scene, sim.object_shape_type, 0)
	local visibleHandles = {}
	if (toRestore==nil) then
		toRestore = {}
	end
	for i = 1, #handles, 1 do
		property=sim.getObjectSpecialProperty(handles[i])
        val = sim.boolAnd32(property, sim.objectspecialproperty_renderable)
		if val>0 then
			simpleShapeHandles=sim.ungroupShape(handles[i])
			--simpleShapeHandles = {handles[i]}
			if #simpleShapeHandles>1 then
				toRestore[#toRestore + 1] = simpleShapeHandles
			end
			for ii = 1, #simpleShapeHandles, 1 do
				visibleHandles[#visibleHandles+1] = simpleShapeHandles[ii]
			end
		end
	end
    handles = sim.getObjectsInTree(sim.handle_scene, sim.object_shape_type, 0)
	numberOfObjects = #handles
	return visibleHandles
end

You can change this code to generate a table visibleHandles, with the meshes you like to be exported.

# Contact
boris.bogaerts@uantwerpen.be