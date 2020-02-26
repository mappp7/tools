//Maya ASCII 2017ff05 scene
//Name: HIKJoint_2018.08.06.ma
//Last modified: Mon, Aug 06, 2018 03:16:07 PM
//Codeset: UTF-8
requires maya "2017ff05";
requires -nodeType "HIKCharacterNode" -nodeType "HIKProperty2State" -dataType "HIKCharacter"
		 -dataType "HIKCharacterState" -dataType "HIKEffectorState" -dataType "HIKPropertySetState"
		 "mayaHIK" "1.0_HIK_2016.5";
requires -nodeType "mentalrayFramebuffer" -nodeType "mentalrayOutputPass" -nodeType "mentalrayRenderPass"
		 -nodeType "mentalrayUserBuffer" -nodeType "mentalraySubdivApprox" -nodeType "mentalrayCurveApprox"
		 -nodeType "mentalraySurfaceApprox" -nodeType "mentalrayDisplaceApprox" -nodeType "mentalrayOptions"
		 -nodeType "mentalrayGlobals" -nodeType "mentalrayItemsList" -nodeType "mentalrayShader"
		 -nodeType "mentalrayUserData" -nodeType "mentalrayText" -nodeType "mentalrayTessellation"
		 -nodeType "mentalrayPhenomenon" -nodeType "mentalrayLightProfile" -nodeType "mentalrayVertexColors"
		 -nodeType "mentalrayIblShape" -nodeType "mapVizShape" -nodeType "mentalrayCCMeshProxy"
		 -nodeType "cylindricalLightLocator" -nodeType "discLightLocator" -nodeType "rectangularLightLocator"
		 -nodeType "sphericalLightLocator" -nodeType "abcimport" -nodeType "mia_physicalsun"
		 -nodeType "mia_physicalsky" -nodeType "mia_material" -nodeType "mia_material_x" -nodeType "mia_roundcorners"
		 -nodeType "mia_exposure_simple" -nodeType "mia_portal_light" -nodeType "mia_light_surface"
		 -nodeType "mia_exposure_photographic" -nodeType "mia_exposure_photographic_rev" -nodeType "mia_lens_bokeh"
		 -nodeType "mia_envblur" -nodeType "mia_ciesky" -nodeType "mia_photometric_light"
		 -nodeType "mib_texture_vector" -nodeType "mib_texture_remap" -nodeType "mib_texture_rotate"
		 -nodeType "mib_bump_basis" -nodeType "mib_bump_map" -nodeType "mib_passthrough_bump_map"
		 -nodeType "mib_bump_map2" -nodeType "mib_lookup_spherical" -nodeType "mib_lookup_cube1"
		 -nodeType "mib_lookup_cube6" -nodeType "mib_lookup_background" -nodeType "mib_lookup_cylindrical"
		 -nodeType "mib_texture_lookup" -nodeType "mib_texture_lookup2" -nodeType "mib_texture_filter_lookup"
		 -nodeType "mib_texture_checkerboard" -nodeType "mib_texture_polkadot" -nodeType "mib_texture_polkasphere"
		 -nodeType "mib_texture_turbulence" -nodeType "mib_texture_wave" -nodeType "mib_reflect"
		 -nodeType "mib_refract" -nodeType "mib_transparency" -nodeType "mib_continue" -nodeType "mib_opacity"
		 -nodeType "mib_twosided" -nodeType "mib_refraction_index" -nodeType "mib_dielectric"
		 -nodeType "mib_ray_marcher" -nodeType "mib_illum_lambert" -nodeType "mib_illum_phong"
		 -nodeType "mib_illum_ward" -nodeType "mib_illum_ward_deriv" -nodeType "mib_illum_blinn"
		 -nodeType "mib_illum_cooktorr" -nodeType "mib_illum_hair" -nodeType "mib_volume"
		 -nodeType "mib_color_alpha" -nodeType "mib_color_average" -nodeType "mib_color_intensity"
		 -nodeType "mib_color_interpolate" -nodeType "mib_color_mix" -nodeType "mib_color_spread"
		 -nodeType "mib_geo_cube" -nodeType "mib_geo_torus" -nodeType "mib_geo_sphere" -nodeType "mib_geo_cone"
		 -nodeType "mib_geo_cylinder" -nodeType "mib_geo_square" -nodeType "mib_geo_instance"
		 -nodeType "mib_geo_instance_mlist" -nodeType "mib_geo_add_uv_texsurf" -nodeType "mib_photon_basic"
		 -nodeType "mib_light_infinite" -nodeType "mib_light_point" -nodeType "mib_light_spot"
		 -nodeType "mib_light_photometric" -nodeType "mib_cie_d" -nodeType "mib_blackbody"
		 -nodeType "mib_shadow_transparency" -nodeType "mib_lens_stencil" -nodeType "mib_lens_clamp"
		 -nodeType "mib_lightmap_write" -nodeType "mib_lightmap_sample" -nodeType "mib_amb_occlusion"
		 -nodeType "mib_fast_occlusion" -nodeType "mib_map_get_scalar" -nodeType "mib_map_get_integer"
		 -nodeType "mib_map_get_vector" -nodeType "mib_map_get_color" -nodeType "mib_map_get_transform"
		 -nodeType "mib_map_get_scalar_array" -nodeType "mib_map_get_integer_array" -nodeType "mib_fg_occlusion"
		 -nodeType "mib_bent_normal_env" -nodeType "mib_glossy_reflection" -nodeType "mib_glossy_refraction"
		 -nodeType "mib_illum_hair_x" -nodeType "builtin_bsdf_architectural" -nodeType "builtin_bsdf_architectural_comp"
		 -nodeType "builtin_bsdf_carpaint" -nodeType "builtin_bsdf_ashikhmin" -nodeType "builtin_bsdf_lambert"
		 -nodeType "builtin_bsdf_mirror" -nodeType "builtin_bsdf_phong" -nodeType "contour_store_function"
		 -nodeType "contour_store_function_simple" -nodeType "contour_contrast_function_levels"
		 -nodeType "contour_contrast_function_simple" -nodeType "contour_shader_simple" -nodeType "contour_shader_silhouette"
		 -nodeType "contour_shader_maxcolor" -nodeType "contour_shader_curvature" -nodeType "contour_shader_factorcolor"
		 -nodeType "contour_shader_depthfade" -nodeType "contour_shader_framefade" -nodeType "contour_shader_layerthinner"
		 -nodeType "contour_shader_widthfromcolor" -nodeType "contour_shader_widthfromlightdir"
		 -nodeType "contour_shader_widthfromlight" -nodeType "contour_shader_combi" -nodeType "contour_only"
		 -nodeType "contour_composite" -nodeType "contour_ps" -nodeType "mi_metallic_paint"
		 -nodeType "mi_metallic_paint_x" -nodeType "mi_bump_flakes" -nodeType "mi_car_paint_phen"
		 -nodeType "mi_metallic_paint_output_mixer" -nodeType "mi_car_paint_phen_x" -nodeType "physical_lens_dof"
		 -nodeType "physical_light" -nodeType "dgs_material" -nodeType "dgs_material_photon"
		 -nodeType "dielectric_material" -nodeType "dielectric_material_photon" -nodeType "oversampling_lens"
		 -nodeType "path_material" -nodeType "parti_volume" -nodeType "parti_volume_photon"
		 -nodeType "transmat" -nodeType "transmat_photon" -nodeType "mip_rayswitch" -nodeType "mip_rayswitch_advanced"
		 -nodeType "mip_rayswitch_environment" -nodeType "mip_card_opacity" -nodeType "mip_motionblur"
		 -nodeType "mip_motion_vector" -nodeType "mip_matteshadow" -nodeType "mip_cameramap"
		 -nodeType "mip_mirrorball" -nodeType "mip_grayball" -nodeType "mip_gamma_gain" -nodeType "mip_render_subset"
		 -nodeType "mip_matteshadow_mtl" -nodeType "mip_binaryproxy" -nodeType "mip_rayswitch_stage"
		 -nodeType "mip_fgshooter" -nodeType "mib_ptex_lookup" -nodeType "misss_physical"
		 -nodeType "misss_physical_phen" -nodeType "misss_fast_shader" -nodeType "misss_fast_shader_x"
		 -nodeType "misss_fast_shader2" -nodeType "misss_fast_shader2_x" -nodeType "misss_skin_specular"
		 -nodeType "misss_lightmap_write" -nodeType "misss_lambert_gamma" -nodeType "misss_call_shader"
		 -nodeType "misss_set_normal" -nodeType "misss_fast_lmap_maya" -nodeType "misss_fast_simple_maya"
		 -nodeType "misss_fast_skin_maya" -nodeType "misss_fast_skin_phen" -nodeType "misss_fast_skin_phen_d"
		 -nodeType "misss_mia_skin2_phen" -nodeType "misss_mia_skin2_phen_d" -nodeType "misss_lightmap_phen"
		 -nodeType "misss_mia_skin2_surface_phen" -nodeType "surfaceSampler" -nodeType "mib_data_bool"
		 -nodeType "mib_data_int" -nodeType "mib_data_scalar" -nodeType "mib_data_vector"
		 -nodeType "mib_data_color" -nodeType "mib_data_string" -nodeType "mib_data_texture"
		 -nodeType "mib_data_shader" -nodeType "mib_data_bool_array" -nodeType "mib_data_int_array"
		 -nodeType "mib_data_scalar_array" -nodeType "mib_data_vector_array" -nodeType "mib_data_color_array"
		 -nodeType "mib_data_string_array" -nodeType "mib_data_texture_array" -nodeType "mib_data_shader_array"
		 -nodeType "mib_data_get_bool" -nodeType "mib_data_get_int" -nodeType "mib_data_get_scalar"
		 -nodeType "mib_data_get_vector" -nodeType "mib_data_get_color" -nodeType "mib_data_get_string"
		 -nodeType "mib_data_get_texture" -nodeType "mib_data_get_shader" -nodeType "mib_data_get_shader_bool"
		 -nodeType "mib_data_get_shader_int" -nodeType "mib_data_get_shader_scalar" -nodeType "mib_data_get_shader_vector"
		 -nodeType "mib_data_get_shader_color" -nodeType "user_ibl_env" -nodeType "user_ibl_rect"
		 -nodeType "xgen_geo" -nodeType "xgen_seexpr" -nodeType "xgen_scalar_to_integer" -nodeType "xgen_integer_to_vector"
		 -nodeType "xgen_scalar_to_vector" -nodeType "xgen_boolean_to_vector" -nodeType "xgen_boolean_switch"
		 -nodeType "xgen_tube_normals" -nodeType "xgen_hair_phen" -nodeType "mia_material_x_passes"
		 -nodeType "mi_metallic_paint_x_passes" -nodeType "mi_car_paint_phen_x_passes" -nodeType "misss_fast_shader_x_passes"
		 -dataType "byteArray" "Mayatomr" "2014.0 - 3.11.1.13 ";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2017";
fileInfo "version" "2017";
fileInfo "cutIdentifier" "201706020738-1017329";
fileInfo "osv" "Linux 3.10.0-123.8.1.el7.x86_64 #1 SMP Mon Sep 22 19:06:58 UTC 2014 x86_64";
createNode transform -s -n "persp";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000238D";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 5.7396087403170686 21.327689232452602 31.593383012171493 ;
	setAttr ".r" -type "double3" -20.738352729602429 8.1999999999999265 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000238E";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 37.712727902730521;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000238F";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 100.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002390";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002391";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 100.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002392";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002393";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 100.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002394";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "mocap_char_GRP";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002395";
createNode transform -n "mocap_char" -p "mocap_char_GRP";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002396";
createNode joint -n "Crw_Hips" -p "mocap_char";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002397";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 0.041268873999999997 8.390645 -0.19978804999999999 ;
	setAttr ".jo" -type "double3" 89.999999999999986 0 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-16 1 0 0 -2.2204460492503131e-16 0 1 0
		 1 -2.2204460492503131e-16 2.2204460492503131e-16 0 0 8.9231745720989668 -0.17376929722515433 1;
	setAttr ".typ" 1;
	setAttr ".radi" 2;
createNode joint -n "Crw_LeftUpLeg" -p "Crw_Hips";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002398";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 -2.2204460492503131e-16 1 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" -3.4450928483976665e-16 -1 -2.7192621468937821e-32 0 -2.2204460492503131e-16 0 1 0
		 -1 3.4450928483976665e-16 -2.2204460492503131e-16 0 1 8.9231745720989668 -0.17376929722515433 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
	setAttr ".radi" 2;
createNode joint -n "Crw_LeftLeg" -p "Crw_LeftUpLeg";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002399";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 4.2716684427277309 2.7755575615628914e-17 -1.8873791418627657e-15 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".bps" -type "matrix" -3.4450928483976665e-16 -1 -2.7192621468937821e-32 0 -2.2204460492503131e-16 0 1 0
		 -1 3.4450928483976665e-16 -2.2204460492503131e-16 0 1.0000000000000004 4.6515061293712359 -0.1737692972251543 1;
	setAttr ".sd" 1;
	setAttr ".typ" 3;
	setAttr ".radi" 2;
createNode joint -n "Crw_LeftFoot" -p "Crw_LeftLeg";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000239A";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 3.8601122635449254 3.6082248300317583e-16 0 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".jo" -type "double3" 1.9891601228648396e-05 3.3421410447133865e-05 61.353142918098186 ;
	setAttr ".bps" -type "matrix" 5.8331365260285755e-07 -0.4794097213532717 0.8775912027086632 0 -3.4717393473770999e-07 0.87759120270866253 0.47940972135350202 0
		 -0.99999999999976963 -5.8432302659159528e-07 3.4547237063040041e-07 0 0.999999999999999 0.79139386582631044 -0.17376929722515394 1;
	setAttr ".sd" 1;
	setAttr ".typ" 4;
	setAttr ".radi" 2;
createNode joint -n "Crw_LeftToeBase" -p "Crw_LeftFoot";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000239B";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 1.3684725807972993 -5.5511151231257827e-16 -2.6533356622948645e-09 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".jo" -type "double3" -5.109432601362014e-06 -2.0010911851502278e-05 28.646857081913563 ;
	setAttr ".bps" -type "matrix" -3.7839275046630266e-09 4.2458395349776781e-16 0.99999999999999989 0 -4.9514660478913793e-07 0.99999999999987732 -2.3307692628111074e-15 0
		 -0.99999999999987743 -4.9514660478913814e-07 -3.7839275046622325e-09 0 1.0000008009020744 0.13533480718668578 1.0271902008305751 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
	setAttr ".radi" 2;
createNode joint -n "Crw_LeftToe" -p "Crw_LeftToeBase";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000239C";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0.86637208112808017 2.2204460492503131e-16 4.4408920985006262e-16 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".bps" -type "matrix" -3.7839275046630266e-09 4.2458395349776781e-16 0.99999999999999989 0 -4.9514660478913793e-07 0.99999999999987732 -2.3307692628111074e-15 0
		 -0.99999999999987743 -4.9514660478913814e-07 -3.7839275046622325e-09 0 1.0000007976237848 0.13533480718668636 1.8935622819586553 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "ToeTip";
	setAttr ".radi" 2;
createNode joint -n "Crw_RightUpLeg" -p "Crw_Hips";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000239D";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -4.5720989660935629e-06 2.972251545441118e-07 -1 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-16 1 0 0 9.9579925010295987e-17 2.7192621468937821e-32 -1 0
		 -1 2.2204460492503131e-16 -9.9579925010295987e-17 0 -1 8.9231700000000007 -0.17376900000000001 1;
	setAttr ".sd" 2;
	setAttr ".typ" 2;
	setAttr ".radi" 2;
createNode joint -n "Crw_RightLeg" -p "Crw_RightUpLeg";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000239E";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -4.2716600000000007 0 -9.9920072216264089e-16 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".bps" -type "matrix" 2.2204460492503131e-16 1 0 0 9.9579925010295987e-17 2.7192621468937821e-32 -1 0
		 -1 2.2204460492503131e-16 -9.9579925010295987e-17 0 -1 4.65151 -0.17376900000000001 1;
	setAttr ".sd" 2;
	setAttr ".typ" 3;
	setAttr ".radi" 2;
createNode joint -n "Crw_RightFoot" -p "Crw_RightLeg";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000239F";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -3.860116 0 -7.7715611723760958e-16 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".jo" -type "double3" 1.9825701656093505e-05 3.3421410415399674e-05 61.353142918098222 ;
	setAttr ".bps" -type "matrix" 5.8331365260285777e-07 0.47940972135327098 -0.87759120270866364 0 -3.4602377056398316e-07 -0.87759120270866364 -0.47940972135350102 0
		 -0.99999999999976996 5.8331365263106153e-07 -3.460237705164382e-07 0 -1 0.79139400000000004 -0.17376900000000001 1;
	setAttr ".sd" 2;
	setAttr ".typ" 4;
	setAttr ".radi" 2;
createNode joint -n "Crw_RightToeBase" -p "Crw_RightFoot";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023A0";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -1.3684721155956827 1.8731120954296188e-07 2.0175146686618461e-07 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".jo" -type "double3" -4.2637256250019054e-06 -2.0042504737796228e-05 28.646857081913513 ;
	setAttr ".bps" -type "matrix" -3.7839275046628148e-09 -6.2200853849649057e-16 -1 0 -5.0889760207317231e-07 -0.99999999999987044 2.4350388838691297e-15 0
		 -0.99999999999987044 5.0889760207317231e-07 3.7839275046620737e-09 0 -1.0000009999999999 0.13533500000000032 1.02719 1;
	setAttr ".sd" 2;
	setAttr ".typ" 5;
	setAttr ".radi" 2;
createNode joint -n "Crw_RightToe" -p "Crw_RightToeBase";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023A1";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -0.86636999999999986 1.9428902930940239e-15 3.2782812020570873e-09 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".bps" -type "matrix" -3.7839275046628148e-09 -6.2200853849649057e-16 -1 0 -5.0889760207317231e-07 -0.99999999999987044 2.4350388838691297e-15 0
		 -0.99999999999987044 5.0889760207317231e-07 3.7839275046620737e-09 0 -1.0000009999999999 0.13533500000000059 1.8935599999999999 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "ToeTip";
	setAttr ".radi" 2;
createNode joint -n "Crw_Spine" -p "Crw_Hips";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023A2";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.58774894329774696 0 -1.3050648190965283e-16 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".bps" -type "matrix" 2.2204460492503131e-16 1 0 0 -2.2204460492503131e-16 0 1 0
		 1 -2.2204460492503131e-16 2.2204460492503131e-16 0 0 9.5109235153967138 -0.17376929722515433 1;
	setAttr ".typ" 6;
	setAttr ".radi" 2;
createNode joint -n "Crw_Spine1" -p "Crw_Spine";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023A3";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0.98930015668563698 0 -2.1966876244353383e-16 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".bps" -type "matrix" 2.2204460492503131e-16 1 0 0 -2.2204460492503131e-16 0 1 0
		 1 -2.2204460492503131e-16 2.2204460492503131e-16 0 0 10.500223672082353 -0.17376929722515433 1;
	setAttr ".typ" 6;
	setAttr ".radi" 2;
createNode joint -n "Crw_Spine2" -p "Crw_Spine1";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023A4";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 1.2035565681447071 0 -2.6724324267861797e-16 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".bps" -type "matrix" 2.2204460492503131e-16 1 0 0 -2.2204460492503131e-16 0 1 0
		 1 -2.2204460492503131e-16 2.2204460492503131e-16 0 0 11.703780240227058 -0.17376929722515433 1;
	setAttr ".typ" 6;
	setAttr ".radi" 2;
createNode joint -n "Crw_Spine3" -p "Crw_Spine2";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023A5";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 1.1721460718394212 0 -2.6026871143601165e-16 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".bps" -type "matrix" 2.2204460492503131e-16 1 0 0 -2.2204460492503131e-16 0 1 0
		 1 -2.2204460492503131e-16 2.2204460492503131e-16 0 0 12.875926312066481 -0.17376929722515433 1;
	setAttr ".typ" 6;
	setAttr ".radi" 2;
createNode joint -n "Crw_Neck" -p "Crw_Spine3";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023A6";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 1.0527813315795027 -7.4940054162198066e-16 -2.337644148430203e-16 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".bps" -type "matrix" 2.2204460492503131e-16 1 0 0 -2.2204460492503131e-16 0 1 0
		 1 -2.2204460492503131e-16 2.2204460492503131e-16 0 -1.035379938102578e-30 13.928707643645982 -0.17376929722515508 1;
	setAttr ".typ" 7;
	setAttr ".radi" 2;
createNode joint -n "Crw_Head" -p "Crw_Neck";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023A7";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 1.4094567464894061 0 -3.1296226643316019e-16 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".bps" -type "matrix" 2.2204460492503131e-16 1 0 0 -2.2204460492503131e-16 0 1 0
		 1 -2.2204460492503131e-16 2.2204460492503131e-16 0 -1.035379938102578e-30 15.338164390135388 -0.17376929722515508 1;
	setAttr ".typ" 8;
	setAttr ".radi" 2;
createNode joint -n "Crw_Hair" -p "Crw_Head";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023A8";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 1.185 0 -3.9443045261050617e-31 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".bps" -type "matrix" 2.2204460492503131e-16 1 0 0 -2.2204460492503131e-16 0 1 0
		 1 -2.2204460492503131e-16 2.2204460492503131e-16 0 3.7841093970218938e-16 17.042375757171094 -0.17376929722515508 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "hair";
	setAttr ".radi" 2;
createNode joint -n "Crw_hairTip" -p "Crw_Hair";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023A9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.306 0.008 6.0748788119921089e-17 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.999999999999986 -89.999999999999986 0 ;
	setAttr ".bps" -type "matrix" 1 0 2.2204460492503131e-16 0 -4.9303806576313238e-32 1 2.2204460492503121e-16 0
		 -2.2204460492503136e-16 -2.2204460492503131e-16 1 0 1.152880828660282e-16 17.197881028695463 1.4403241938392934 1;
	setAttr ".radi" 2;
createNode joint -n "Crw_LeftShoulder" -p "Crw_Spine3";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023AA";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0.65167368793352054 2.9722515418328932e-07 0.6441929999999999 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".jo" -type "double3" -89.999999999999986 -89.999999999999986 0 ;
	setAttr ".bps" -type "matrix" 1 0 2.2204460492503131e-16 0 -4.9303806576313238e-32 1 2.2204460492503126e-16 0
		 -2.2204460492503136e-16 -2.2204460492503131e-16 1 0 0.64419300000000002 13.5276 -0.17376900000000001 1;
	setAttr ".sd" 1;
	setAttr ".typ" 9;
	setAttr ".radi" 2;
createNode joint -n "Crw_LeftArm" -p "Crw_LeftShoulder";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023AB";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0.970867 -0.014999999999998792 0 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".bps" -type "matrix" 1 0 2.2204460492503131e-16 0 -4.9303806576313238e-32 1 2.2204460492503126e-16 0
		 -2.2204460492503136e-16 -2.2204460492503131e-16 1 0 1.6150599999999999 13.512600000000001 -0.17376899999999978 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
	setAttr ".radi" 2;
createNode joint -n "Crw_LeftForeArm" -p "Crw_LeftArm";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023AC";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 2.8141100000000003 0 0 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".pa" -type "double3" 0 -1 0 ;
	setAttr ".bps" -type "matrix" 1 0 2.2204460492503131e-16 0 -4.9303806576313238e-32 1 2.2204460492503126e-16 0
		 -2.2204460492503136e-16 -2.2204460492503131e-16 1 0 4.4291700000000001 13.512600000000001 -0.17376899999999915 1;
	setAttr ".sd" 1;
	setAttr ".typ" 11;
	setAttr ".radi" 2;
createNode joint -n "Crw_LeftHand" -p "Crw_LeftForeArm";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023AD";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 2.5164999999999997 0 0 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".bps" -type "matrix" 1 0 2.2204460492503131e-16 0 -4.9303806576313238e-32 1 2.2204460492503126e-16 0
		 -2.2204460492503136e-16 -2.2204460492503131e-16 1 0 6.9456699999999998 13.512600000000001 -0.17376899999999859 1;
	setAttr ".sd" 1;
	setAttr ".typ" 12;
	setAttr ".radi" 2;
createNode joint -n "Crw_LefthandSub1" -p "Crw_LeftHand";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023AE";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.82957000000000036 0 0 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".bps" -type "matrix" 1 0 2.2204460492503131e-16 0 -4.9303806576313238e-32 1 2.2204460492503126e-16 0
		 -2.2204460492503136e-16 -2.2204460492503131e-16 1 0 7.7752400000000002 13.512600000000001 -0.1737689999999984 1;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
	setAttr ".radi" 2;
createNode joint -n "Crw_LefthandSub2" -p "Crw_LefthandSub1";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023AF";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0.93052999999999919 -0.4 -2.7755575615628914e-17 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".bps" -type "matrix" 1 0 2.2204460492503131e-16 0 -4.9303806576313238e-32 1 2.2204460492503126e-16 0
		 -2.2204460492503136e-16 -2.2204460492503131e-16 1 0 8.7057699999999993 13.1126 -0.17376899999999831 1;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
	setAttr ".radi" 2;
createNode joint -n "Crw_RightShoulder" -p "Crw_Spine3";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023B0";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0.65167368793352054 2.9722515446084508e-07 -0.64419300000000013 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".jo" -type "double3" 90.000000000000014 -89.999999999999986 0 ;
	setAttr ".bps" -type "matrix" 1 0 2.2204460492503131e-16 0 4.9303806576313238e-32 -1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 -1 0 -0.64419300000000002 13.5276 -0.17376900000000001 1;
	setAttr ".sd" 2;
	setAttr ".typ" 9;
	setAttr ".radi" 2;
createNode joint -n "Crw_RightArm" -p "Crw_RightShoulder";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023B1";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -0.970867 0.014999999999998792 0 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".bps" -type "matrix" 1 0 2.2204460492503131e-16 0 4.9303806576313238e-32 -1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 -1 0 -1.6150599999999999 13.512600000000001 -0.17376900000000023 1;
	setAttr ".sd" 2;
	setAttr ".typ" 10;
	setAttr ".radi" 2;
createNode joint -n "Crw_RightForeArm" -p "Crw_RightArm";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023B2";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -2.8141100000000003 0 0 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".pa" -type "double3" 0 -1 0 ;
	setAttr ".bps" -type "matrix" 1 0 2.2204460492503131e-16 0 4.9303806576313238e-32 -1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 -1 0 -4.4291700000000001 13.512600000000001 -0.17376900000000087 1;
	setAttr ".sd" 2;
	setAttr ".typ" 11;
	setAttr ".radi" 2;
createNode joint -n "Crw_RightHand" -p "Crw_RightForeArm";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023B3";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" -2.5164999999999997 0 0 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".bps" -type "matrix" 1 0 2.2204460492503131e-16 0 4.9303806576313238e-32 -1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 -1 0 -6.9456699999999998 13.512600000000001 -0.17376900000000142 1;
	setAttr ".sd" 2;
	setAttr ".typ" 12;
	setAttr ".radi" 2;
createNode joint -n "Crw_RightHandSub1" -p "Crw_RightHand";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023B4";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -0.82957000000000036 0 0 ;
	setAttr -av ".rx";
	setAttr -av ".ry";
	setAttr -av ".rz";
	setAttr ".bps" -type "matrix" 1 0 2.2204460492503131e-16 0 4.9303806576313238e-32 -1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 -1 0 -7.7752400000000002 13.512600000000001 -0.17376900000000162 1;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
	setAttr ".radi" 2;
createNode joint -n "Crw_RightHandSub2" -p "Crw_RightHandSub1";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023B5";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -0.93052999999999919 0.4 0 ;
	setAttr ".bps" -type "matrix" 1 0 2.2204460492503131e-16 0 4.9303806576313238e-32 -1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 -1 0 -8.7057699999999993 13.1126 -0.17376900000000192 1;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
	setAttr ".radi" 2;
createNode transform -n "mocap_geometry_GRP" -p "mocap_char_GRP";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023B6";
createNode transform -n "mocap_shirt_PLY" -p "mocap_geometry_GRP";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023B7";
	setAttr ".ove" yes;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode mesh -n "mocap_shirt_PLYShape" -p "mocap_shirt_PLY";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023B8";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ugsdt" no;
	setAttr ".vs" 6;
	setAttr ".bw" 6;
	setAttr ".vcs" 2;
createNode mesh -n "polySurfaceShape2" -p "mocap_shirt_PLY";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023B9";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ugsdt" no;
	setAttr -s 177 ".vt";
	setAttr ".vt[0:165]"  0 14.42501545 -0.784545 0 14.021024704 -1.043285012
		 0 13.40347385 -1.20146203 0 12.71088886 -1.15994203 0 11.94692326 -1.17070997 0 9.1499567 -1.19271684
		 0 8.89008236 -1.15266597 0 12.65693283 1.31544626 0 13.57014656 0.96093303 0 9.0163517 1.65854704
		 0 8.70031452 1.32385802 1.019544005 14.32876778 -0.119789 1.98429298 14.13594723 -0.25560901
		 0.72563797 14.049445152 -0.99997699 0.493038 14.422575 -0.69010699 0.99764597 14.041020393 0.33802199
		 0.87115246 12.58696747 1.21868873 0.815651 13.51596832 0.77785897 0 13.74206448 0.75586843
		 1.58701384 12.60463047 0.83222145 1.459782 12.7561636 -1.0070220232 1.62871397 12.01088047 -0.59739399
		 1.35196602 13.43617535 -1.11205304 0.82378298 12.71024895 -1.22548902 0.87538999 11.97943878 -1.10555995
		 0.79046398 13.409091 -1.22975898 1.79056299 11.98830986 0.13768385 1.27019405 14.11419773 -0.81338102
		 0.79685497 9.054486275 1.48757899 1.52611101 9.12343693 0.99441803 1.79476202 9.17762852 0.40790701
		 1.79930699 9.16509151 -0.31891599 1.096377969 9.17743015 -1.17896485 0.70468599 8.70031452 1.27147603
		 1.41819799 8.7749567 0.84201801 1.64284205 8.86343098 0.34358701 1.60871506 8.89620113 -0.28389701
		 0.989456 8.87362099 -1.086969972 1.98429298 13.45046329 -0.95908803 1.98429298 13.92981339 -0.78305501
		 1.98429298 12.94450665 -0.83231997 1.99971497 12.57087326 -0.450461 1.96349585 13.040336609 0.51745147
		 1.98249876 13.90034008 0.18878663 1.98512626 12.66146278 0.14609112 1.97860825 13.47399807 0.52359313
		 0.82938999 14.40751362 -0.488778 0 10.64893913 -1.077801585 1.039451957 10.64796734 -0.96956754
		 1.62764096 10.71965599 -0.34895 1.66403258 10.76782322 0.34831601 1.39263427 10.77726269 0.92826998
		 0.76678187 10.71638966 1.51712298 0 10.69198704 1.68800199 1.44892132 13.36983299 0.70634007
		 1.42042959 13.90286064 0.30590338 1.41435695 14.1861763 -0.20114601 3.35270691 12.79228878 -0.018215001
		 3.358078 12.98247147 0.242458 3.35802388 13.44903564 0.37299901 3.35804296 13.89978313 0.14208201
		 3.35813808 13.98430634 -0.198725 3.35830498 13.86216545 -0.60580897 3.35845304 13.43713379 -0.84139699
		 3.35844803 13.001991272 -0.79454798 3.35284209 12.80206776 -0.418993 0.54466999 13.89935684 0.630225
		 0.65555501 14.27781773 0.300459 0.74779499 14.53408623 -0.121206 0.57108003 14.6047287 -0.426135
		 0.409574 14.56598473 -0.58638299 0 14.56502724 -0.68239999 2.590734 14.066104889 -0.231163
		 2.59073305 13.88199425 0.146971 2.59073305 13.88666153 -0.68768698 2.59073305 13.46283722 -0.91310698
		 2.59073305 12.98693752 -0.80680501 2.58559299 12.67920113 -0.42002499 2.58821869 12.72143459 0.07694269
		 2.59499288 13.01617527 0.35044548 2.59112597 13.46259117 0.39699292 1.73859751 12.77891731 0.65728134
		 1.86117601 12.31045628 0.14247872 1.83981502 12.34336948 -0.51601303 1.78944898 12.86080742 -0.904028
		 1.774104 13.43244171 -1.032544971 1.76095295 14.022191048 -0.78503102 1.77853501 14.16166401 -0.236643
		 1.77972186 13.88446903 0.25407532 1.77041328 13.40912247 0.62670553 0.5623126 14.13156414 0.15149054
		 0.62512863 14.36074352 -0.16486412 0.50286651 13.77035427 0.44615451 -3.9581209e-08 13.61453724 0.5630098
		 0.45585039 14.4317379 -0.34075579 0.34099978 14.41464424 -0.42949051 3.9581209e-08 14.42367172 -0.50403523
		 -1.019544005 14.32876778 -0.119789 -1.98429298 14.13594723 -0.25560901 -0.72563797 14.049445152 -0.99997699
		 -0.493038 14.422575 -0.69010699 -0.99764597 14.041020393 0.33802199 -0.87115246 12.58696747 1.21868873
		 -0.815651 13.51596832 0.77785897 -1.58701384 12.60463047 0.83222145 -1.459782 12.7561636 -1.0070220232
		 -1.62871397 12.01088047 -0.59739399 -1.35196602 13.43617535 -1.11205304 -0.82378298 12.71024895 -1.22548902
		 -0.87538999 11.97943878 -1.10555995 -0.79046398 13.409091 -1.22975898 -1.79056299 11.98830986 0.13768385
		 -1.27019405 14.11419773 -0.81338102 -0.79685497 9.054486275 1.48757899 -1.52611101 9.12343693 0.99441803
		 -1.79476202 9.17762852 0.40790701 -1.79930699 9.16509151 -0.31891599 -1.096377969 9.17743015 -1.17896485
		 -0.70468599 8.70031452 1.27147603 -1.41819799 8.7749567 0.84201801 -1.64284205 8.86343098 0.34358701
		 -1.60871506 8.89620113 -0.28389701 -0.989456 8.87362099 -1.086969972 -1.98429298 13.45046329 -0.95908803
		 -1.98429298 13.92981339 -0.78305501 -1.98429298 12.94450665 -0.83231997 -1.99971497 12.57087326 -0.450461
		 -1.96349585 13.040336609 0.51745147 -1.98249876 13.90034008 0.18878663 -1.98512626 12.66146278 0.14609112
		 -1.97860825 13.47399807 0.52359313 -0.82938999 14.40751362 -0.488778 -1.039451957 10.64796734 -0.96956754
		 -1.62764096 10.71965599 -0.34895 -1.66403258 10.76782322 0.34831601 -1.39263427 10.77726269 0.92826998
		 -0.76678187 10.71638966 1.51712298 -1.44892132 13.36983299 0.70634007 -1.42042959 13.90286064 0.30590338
		 -1.41435695 14.1861763 -0.20114601 -3.35270691 12.79228878 -0.018215001 -3.358078 12.98247147 0.242458
		 -3.35802388 13.44903564 0.37299901 -3.35804296 13.89978313 0.14208201 -3.35813808 13.98430634 -0.198725
		 -3.35830498 13.86216545 -0.60580897 -3.35845304 13.43713379 -0.84139699 -3.35844803 13.001991272 -0.79454798
		 -3.35284209 12.80206776 -0.418993 -0.54466999 13.89935684 0.630225 -0.65555501 14.27781773 0.300459
		 -0.74779499 14.53408623 -0.121206 -0.57108003 14.6047287 -0.426135 -0.409574 14.56598473 -0.58638299
		 -2.590734 14.066104889 -0.231163 -2.59073305 13.88199425 0.146971 -2.59073305 13.88666153 -0.68768698
		 -2.59073305 13.46283722 -0.91310698 -2.59073305 12.98693752 -0.80680501 -2.58559299 12.67920113 -0.42002499
		 -2.58821869 12.72143459 0.07694269 -2.59499288 13.01617527 0.35044548 -2.59112597 13.46259117 0.39699292
		 -1.73859751 12.77891731 0.65728134 -1.86117601 12.31045628 0.14247872 -1.83981502 12.34336948 -0.51601303;
	setAttr ".vt[166:176]" -1.78944898 12.86080742 -0.904028 -1.774104 13.43244171 -1.032544971
		 -1.76095295 14.022191048 -0.78503102 -1.77853501 14.16166401 -0.236643 -1.77972186 13.88446903 0.25407532
		 -1.77041328 13.40912247 0.62670553 -0.5623126 14.13156414 0.15149054 -0.62512863 14.36074352 -0.16486412
		 -0.50286651 13.77035427 0.44615451 -0.45585039 14.4317379 -0.34075579 -0.34099978 14.41464424 -0.42949051;
	setAttr -s 337 ".ed";
	setAttr ".ed[0:165]"  39 12 1 12 72 1 72 74 1 74 39 1 38 39 1 74 75 1 75 38 1
		 40 38 1 75 76 1 76 40 1 42 44 1 44 78 1 78 79 1 79 42 1 12 43 1 43 73 1 73 72 1 43 45 1
		 45 80 1 80 73 1 44 41 1 41 77 1 77 78 1 45 42 1 79 80 1 41 40 1 76 77 1 56 11 1 11 15 1
		 15 55 1 55 56 1 67 68 1 14 46 1 46 27 1 27 13 1 13 14 1 15 17 1 17 54 1 54 55 1 5 47 1
		 47 48 1 48 32 1 32 5 1 48 49 1 49 31 1 31 32 1 8 17 1 17 66 1 66 18 1 18 8 1 69 70 1
		 4 24 1 24 21 1 66 67 1 0 14 1 13 1 1 1 0 1 25 2 1 2 1 1 13 25 1 17 16 1 16 19 1 19 54 1
		 24 23 1 23 20 1 20 21 1 22 20 1 23 25 1 25 22 1 4 3 1 3 23 1 3 2 1 49 50 1 50 30 1
		 30 31 1 21 26 1 26 19 1 50 51 1 51 29 1 29 30 1 7 53 1 16 7 1 52 53 1 53 9 1 9 28 1
		 28 52 1 28 29 1 51 52 1 27 22 1 9 10 1 10 33 0 33 28 1 33 34 0 34 29 1 34 35 0 35 30 1
		 35 36 0 36 31 1 36 37 0 37 32 1 6 5 1 37 6 0 41 83 1 83 84 1 84 40 1 82 44 1 42 81 1
		 81 82 1 82 83 1 84 85 1 85 38 1 85 86 1 86 39 1 8 7 1 68 69 1 86 87 1 87 12 1 70 71 1
		 46 11 1 56 27 1 47 4 1 24 48 1 21 49 1 26 50 1 19 51 1 16 52 1 45 89 1 89 81 1 88 89 1
		 43 88 1 87 88 1 15 67 1 11 68 1 46 69 1 14 70 1 0 71 1 73 60 1 60 61 0 61 72 1 61 62 0
		 62 74 1 62 63 0 63 75 1 63 64 0 64 76 1 64 65 0 65 77 1 65 57 0 57 78 1 57 58 0 58 79 1
		 58 59 0 59 80 1 59 60 0 26 82 1 81 19 1 21 83 1 20 84 1 22 85 1 27 86 1 56 87 1 55 88 1
		 54 89 1 67 90 1 68 91 1 90 91 0;
	setAttr ".ed[166:331]" 66 92 1 18 93 1 92 93 0 69 94 1 70 95 1 94 95 0 92 90 0
		 91 94 0 71 96 1 95 96 0 124 98 1 98 154 1 154 156 1 156 124 1 123 124 1 156 157 1
		 157 123 1 125 123 1 157 158 1 158 125 1 127 129 1 129 160 1 160 161 1 161 127 1 98 128 1
		 128 155 1 155 154 1 128 130 1 130 162 1 162 155 1 129 126 1 126 159 1 159 160 1 130 127 1
		 161 162 1 126 125 1 158 159 1 139 97 1 97 101 1 101 138 1 138 139 1 150 151 1 100 131 1
		 131 112 1 112 99 1 99 100 1 101 103 1 103 137 1 137 138 1 47 132 1 132 117 1 117 5 1
		 132 133 1 133 116 1 116 117 1 8 103 1 103 149 1 149 18 1 152 153 1 4 109 1 109 106 1
		 149 150 1 0 100 1 99 1 1 110 2 1 99 110 1 103 102 1 102 104 1 104 137 1 109 108 1
		 108 105 1 105 106 1 107 105 1 108 110 1 110 107 1 3 108 1 133 134 1 134 115 1 115 116 1
		 106 111 1 111 104 1 134 135 1 135 114 1 114 115 1 102 7 1 136 53 1 9 113 1 113 136 1
		 113 114 1 135 136 1 112 107 1 10 118 0 118 113 1 118 119 0 119 114 1 119 120 0 120 115 1
		 120 121 0 121 116 1 121 122 0 122 117 1 122 6 0 126 165 1 165 166 1 166 125 1 164 129 1
		 127 163 1 163 164 1 164 165 1 166 167 1 167 123 1 167 168 1 168 124 1 151 152 1 168 169 1
		 169 98 1 153 71 1 131 97 1 139 112 1 109 132 1 106 133 1 111 134 1 104 135 1 102 136 1
		 130 171 1 171 163 1 170 171 1 128 170 1 169 170 1 101 150 1 97 151 1 131 152 1 100 153 1
		 155 143 1 143 144 0 144 154 1 144 145 0 145 156 1 145 146 0 146 157 1 146 147 0 147 158 1
		 147 148 0 148 159 1 148 140 0 140 160 1 140 141 0 141 161 1 141 142 0 142 162 1 142 143 0
		 111 164 1 163 104 1 106 165 1 105 166 1 107 167 1 112 168 1 139 169 1 138 170 1 137 171 1
		 150 172 1 151 173 1 172 173 0 149 174 1 174 93 0 152 175 1;
	setAttr ".ed[332:336]" 153 176 1 175 176 0 174 172 0 173 175 0 176 96 0;
	setAttr -s 158 -ch 632 ".fc[0:157]" -type "polyFaces" 
		f 4 0 1 2 3
		f 4 4 -4 5 6
		f 4 7 -7 8 9
		f 4 10 11 12 13
		f 4 14 15 16 -2
		f 4 17 18 19 -16
		f 4 20 21 22 -12
		f 4 23 -14 24 -19
		f 4 25 -10 26 -22
		f 4 27 28 29 30
		f 4 32 33 34 35
		f 4 36 37 38 -30
		f 4 39 40 41 42
		f 4 43 44 45 -42
		f 4 46 47 48 49
		f 4 51 121 -41 120
		f 4 52 122 -44 -122
		f 4 54 -36 55 56
		f 4 57 58 -56 59
		f 4 -38 60 61 62
		f 4 -53 63 64 65
		f 4 66 -65 67 68
		f 4 -52 69 70 -64
		f 4 -71 71 -58 -68
		f 4 72 73 74 -45
		f 4 75 123 -73 -123
		f 4 76 124 -78 -124
		f 4 77 78 79 -74
		f 4 81 80 -83 -126
		f 4 82 83 84 85
		f 4 -62 125 -88 -125
		f 4 -86 86 -79 87
		f 4 -69 -60 -35 88
		f 4 -85 89 90 91
		f 4 -92 92 93 -87
		f 4 -80 -94 94 95
		f 4 -75 -96 96 97
		f 4 -46 -98 98 99
		f 4 100 -43 -100 101
		f 4 102 103 104 -26
		f 4 105 -11 106 107
		f 4 -103 -21 -106 108
		f 4 -105 109 110 -8
		f 4 -111 111 112 -5
		f 4 -61 -47 113 -82
		f 4 -1 -113 115 116
		f 4 118 -28 119 -34
		f 4 126 127 -107 -24
		f 4 128 -127 -18 129
		f 4 -117 130 -130 -15
		f 4 131 -54 -48 -37
		f 4 132 -32 -132 -29
		f 4 133 -115 -133 -119
		f 4 134 -51 -134 -33
		f 4 -118 -135 -55 135
		f 4 -17 136 137 138
		f 4 -3 -139 139 140
		f 4 -6 -141 141 142
		f 4 -9 -143 143 144
		f 4 -27 -145 145 146
		f 4 -23 -147 147 148
		f 4 -13 -149 149 150
		f 4 -25 -151 151 152
		f 4 -20 -153 153 -137
		f 4 154 -108 155 -77
		f 4 156 -109 -155 -76
		f 4 -104 -157 -66 157
		f 4 -110 -158 -67 158
		f 4 -112 -159 -89 159
		f 4 -116 -160 -120 160
		f 4 -131 -161 -31 161
		f 4 -39 162 -129 -162
		f 4 -128 -163 -63 -156
		f 4 31 164 -166 -164
		f 4 -49 166 168 -168
		f 4 50 170 -172 -170
		f 4 53 163 -173 -167
		f 4 114 169 -174 -165
		f 4 117 174 -176 -171
		f 4 -180 -179 -178 -177
		f 4 -183 -182 179 -181
		f 4 -186 -185 182 -184
		f 4 -190 -189 -188 -187
		f 4 177 -193 -192 -191
		f 4 191 -196 -195 -194
		f 4 187 -199 -198 -197
		f 4 194 -201 189 -200
		f 4 197 -203 185 -202
		f 4 -207 -206 -205 -204
		f 4 -212 -211 -210 -209
		f 4 205 -215 -214 -213
		f 4 -218 -217 -216 -40
		f 4 216 -221 -220 -219
		f 4 -50 -224 -223 -222
		f 4 -121 215 -286 -226
		f 4 285 218 -287 -227
		f 4 -57 -230 211 -229
		f 4 -232 229 -59 -231
		f 4 -235 -234 -233 213
		f 4 -238 -237 -236 226
		f 4 -241 -240 236 -239
		f 4 235 -242 -70 225
		f 4 239 230 -72 241
		f 4 219 -245 -244 -243
		f 4 286 242 -288 -246
		f 4 287 247 -289 -247
		f 4 243 -250 -249 -248
		f 4 289 251 -81 -251
		f 4 -254 -253 -84 -252
		f 4 288 255 -290 233
		f 4 -256 248 -255 253
		f 4 -257 210 231 240
		f 4 -259 -258 -90 252
		f 4 254 -261 -260 258
		f 4 -263 -262 260 249
		f 4 -265 -264 262 244
		f 4 -267 -266 264 220
		f 4 -268 266 217 -101
		f 4 201 -271 -270 -269
		f 4 -274 -273 186 -272
		f 4 -275 271 196 268
		f 4 183 -277 -276 270
		f 4 180 -279 -278 276
		f 4 250 -114 221 232
		f 4 -282 -281 278 176
		f 4 209 -285 203 -284
		f 4 199 272 -292 -291
		f 4 -294 193 290 -293
		f 4 190 293 -295 281
		f 4 212 222 227 -296
		f 4 204 295 207 -297
		f 4 283 296 279 -298
		f 4 208 297 224 -299
		f 4 -136 228 298 282
		f 4 -302 -301 -300 192
		f 4 -304 -303 301 178
		f 4 -306 -305 303 181
		f 4 -308 -307 305 184
		f 4 -310 -309 307 202
		f 4 -312 -311 309 198
		f 4 -314 -313 311 188
		f 4 -316 -315 313 200
		f 4 299 -317 315 195
		f 4 246 -319 273 -318
		f 4 245 317 274 -320
		f 4 -321 237 319 269
		f 4 -322 238 320 275
		f 4 -323 256 321 277
		f 4 -324 284 322 280
		f 4 -325 206 323 294
		f 4 324 292 -326 214
		f 4 318 234 325 291
		f 4 326 328 -328 -208
		f 4 167 -331 -330 223
		f 4 331 333 -333 -225
		f 4 329 334 -327 -228
		f 4 327 335 -332 -280
		f 4 332 336 -175 -283;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vs" 6;
	setAttr ".bw" 6;
createNode mesh -n "mocap_shirt_PLYShapeOrig" -p "mocap_shirt_PLY";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023BA";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ugsdt" no;
	setAttr -s 177 ".vt";
	setAttr ".vt[0:165]"  0 14.42501545 -0.784545 0 14.021024704 -1.043285012
		 0 13.40347385 -1.20146203 0 12.71088886 -1.15994203 0 11.94692326 -1.17070997 0 9.1499567 -1.19271684
		 0 8.89008236 -1.15266597 0 12.65693283 1.31544626 0 13.57014656 0.96093303 0 9.0163517 1.65854704
		 0 8.70031452 1.32385802 1.019544005 14.32876778 -0.119789 1.98429298 14.13594723 -0.25560901
		 0.72563797 14.049445152 -0.99997699 0.493038 14.422575 -0.69010699 0.99764597 14.041020393 0.33802199
		 0.87115246 12.58696747 1.21868873 0.815651 13.51596832 0.77785897 0 13.74206448 0.75586843
		 1.58701384 12.60463047 0.83222145 1.459782 12.7561636 -1.0070220232 1.62871397 12.01088047 -0.59739399
		 1.35196602 13.43617535 -1.11205304 0.82378298 12.71024895 -1.22548902 0.87538999 11.97943878 -1.10555995
		 0.79046398 13.409091 -1.22975898 1.79056299 11.98830986 0.13768385 1.27019405 14.11419773 -0.81338102
		 0.79685497 9.054486275 1.48757899 1.52611101 9.12343693 0.99441803 1.79476202 9.17762852 0.40790701
		 1.79930699 9.16509151 -0.31891599 1.096377969 9.17743015 -1.17896485 0.70468599 8.70031452 1.27147603
		 1.41819799 8.7749567 0.84201801 1.64284205 8.86343098 0.34358701 1.60871506 8.89620113 -0.28389701
		 0.989456 8.87362099 -1.086969972 1.98429298 13.45046329 -0.95908803 1.98429298 13.92981339 -0.78305501
		 1.98429298 12.94450665 -0.83231997 1.99971497 12.57087326 -0.450461 1.96349585 13.040336609 0.51745147
		 1.98249876 13.90034008 0.18878663 1.98512626 12.66146278 0.14609112 1.97860825 13.47399807 0.52359313
		 0.82938999 14.40751362 -0.488778 0 10.64893913 -1.077801585 1.039451957 10.64796734 -0.96956754
		 1.62764096 10.71965599 -0.34895 1.66403258 10.76782322 0.34831601 1.39263427 10.77726269 0.92826998
		 0.76678187 10.71638966 1.51712298 0 10.69198704 1.68800199 1.44892132 13.36983299 0.70634007
		 1.42042959 13.90286064 0.30590338 1.41435695 14.1861763 -0.20114601 3.35270691 12.79228878 -0.018215001
		 3.358078 12.98247147 0.242458 3.35802388 13.44903564 0.37299901 3.35804296 13.89978313 0.14208201
		 3.35813808 13.98430634 -0.198725 3.35830498 13.86216545 -0.60580897 3.35845304 13.43713379 -0.84139699
		 3.35844803 13.001991272 -0.79454798 3.35284209 12.80206776 -0.418993 0.54466999 13.89935684 0.630225
		 0.65555501 14.27781773 0.300459 0.74779499 14.53408623 -0.121206 0.57108003 14.6047287 -0.426135
		 0.409574 14.56598473 -0.58638299 0 14.56502724 -0.68239999 2.590734 14.066104889 -0.231163
		 2.59073305 13.89396 0.20493855 2.59073305 13.88666153 -0.68768698 2.59073305 13.46283722 -0.91310698
		 2.59073305 12.98693752 -0.80680501 2.58559299 12.67920113 -0.42002499 2.58821869 12.72143459 0.07694269
		 2.59499288 13.01617527 0.35044548 2.59112597 13.47455692 0.45496047 1.73859751 12.77891731 0.65728134
		 1.86117601 12.31045628 0.14247872 1.83981502 12.34336948 -0.51601303 1.78944898 12.86080742 -0.904028
		 1.774104 13.43244171 -1.032544971 1.76095295 14.022191048 -0.78503102 1.77853501 14.16166401 -0.236643
		 1.77972186 13.88446903 0.25407532 1.77041328 13.40912247 0.62670553 0.5623126 14.13156414 0.15149054
		 0.62512863 14.36074352 -0.16486412 0.50286651 13.77035427 0.44615451 -3.9581209e-08 13.61453724 0.5630098
		 0.45585039 14.4317379 -0.34075579 0.34099978 14.41464424 -0.42949051 3.9581209e-08 14.42367172 -0.50403523
		 -1.019544005 14.32876778 -0.119789 -1.98429298 14.13594723 -0.25560901 -0.72563797 14.049445152 -0.99997699
		 -0.493038 14.422575 -0.69010699 -0.99764597 14.041020393 0.33802199 -0.87115246 12.58696747 1.21868873
		 -0.815651 13.51596832 0.77785897 -1.58701384 12.60463047 0.83222145 -1.459782 12.7561636 -1.0070220232
		 -1.62871397 12.01088047 -0.59739399 -1.35196602 13.43617535 -1.11205304 -0.82378298 12.71024895 -1.22548902
		 -0.87538999 11.97943878 -1.10555995 -0.79046398 13.409091 -1.22975898 -1.79056299 11.98830986 0.13768385
		 -1.27019405 14.11419773 -0.81338102 -0.79685497 9.054486275 1.48757899 -1.52611101 9.12343693 0.99441803
		 -1.79476202 9.17762852 0.40790701 -1.79930699 9.16509151 -0.31891599 -1.096377969 9.17743015 -1.17896485
		 -0.70468599 8.70031452 1.27147603 -1.41819799 8.7749567 0.84201801 -1.64284205 8.86343098 0.34358701
		 -1.60871506 8.89620113 -0.28389701 -0.989456 8.87362099 -1.086969972 -1.98429298 13.45046329 -0.95908803
		 -1.98429298 13.92981339 -0.78305501 -1.98429298 12.94450665 -0.83231997 -1.99971497 12.57087326 -0.450461
		 -1.96349585 13.040336609 0.51745147 -1.98249876 13.90034008 0.18878663 -1.98512626 12.66146278 0.14609112
		 -1.97860825 13.47399807 0.52359313 -0.82938999 14.40751362 -0.488778 -1.039451957 10.64796734 -0.96956754
		 -1.62764096 10.71965599 -0.34895 -1.66403258 10.76782322 0.34831601 -1.39263427 10.77726269 0.92826998
		 -0.76678187 10.71638966 1.51712298 -1.44892132 13.36983299 0.70634007 -1.42042959 13.90286064 0.30590338
		 -1.41435695 14.1861763 -0.20114601 -3.35270691 12.79228878 -0.018215001 -3.358078 12.98247147 0.242458
		 -3.35802388 13.44903564 0.37299901 -3.35804296 13.89978313 0.14208201 -3.35813808 13.98430634 -0.198725
		 -3.35830498 13.86216545 -0.60580897 -3.35845304 13.43713379 -0.84139699 -3.35844803 13.001991272 -0.79454798
		 -3.35284209 12.80206776 -0.418993 -0.54466999 13.89935684 0.630225 -0.65555501 14.27781773 0.300459
		 -0.74779499 14.53408623 -0.121206 -0.57108003 14.6047287 -0.426135 -0.409574 14.56598473 -0.58638299
		 -2.590734 14.066104889 -0.231163 -2.59073305 13.89396 0.20493855 -2.59073305 13.88666153 -0.68768698
		 -2.59073305 13.46283722 -0.91310698 -2.59073305 12.98693752 -0.80680501 -2.58559299 12.67920113 -0.42002499
		 -2.58821869 12.72143459 0.07694269 -2.59499288 13.01617527 0.35044548 -2.59112597 13.47455692 0.45496047
		 -1.73859751 12.77891731 0.65728134 -1.86117601 12.31045628 0.14247872 -1.83981502 12.34336948 -0.51601303;
	setAttr ".vt[166:176]" -1.78944898 12.86080742 -0.904028 -1.774104 13.43244171 -1.032544971
		 -1.76095295 14.022191048 -0.78503102 -1.77853501 14.16166401 -0.236643 -1.77972186 13.88446903 0.25407532
		 -1.77041328 13.40912247 0.62670553 -0.5623126 14.13156414 0.15149054 -0.62512863 14.36074352 -0.16486412
		 -0.50286651 13.77035427 0.44615451 -0.45585039 14.4317379 -0.34075579 -0.34099978 14.41464424 -0.42949051;
	setAttr -s 337 ".ed";
	setAttr ".ed[0:165]"  39 12 1 12 72 1 72 74 1 74 39 1 38 39 1 74 75 1 75 38 1
		 40 38 1 75 76 1 76 40 1 42 44 1 44 78 1 78 79 1 79 42 1 12 43 1 43 73 1 73 72 1 43 45 1
		 45 80 1 80 73 1 44 41 1 41 77 1 77 78 1 45 42 1 79 80 1 41 40 1 76 77 1 56 11 1 11 15 1
		 15 55 1 55 56 1 67 68 1 14 46 1 46 27 1 27 13 1 13 14 1 15 17 1 17 54 1 54 55 1 5 47 1
		 47 48 1 48 32 1 32 5 1 48 49 1 49 31 1 31 32 1 8 17 1 17 66 1 66 18 1 18 8 1 69 70 1
		 4 24 1 24 21 1 66 67 1 0 14 1 13 1 1 1 0 1 25 2 1 2 1 1 13 25 1 17 16 1 16 19 1 19 54 1
		 24 23 1 23 20 1 20 21 1 22 20 1 23 25 1 25 22 1 4 3 1 3 23 1 3 2 1 49 50 1 50 30 1
		 30 31 1 21 26 1 26 19 1 50 51 1 51 29 1 29 30 1 7 53 1 16 7 1 52 53 1 53 9 1 9 28 1
		 28 52 1 28 29 1 51 52 1 27 22 1 9 10 1 10 33 0 33 28 1 33 34 0 34 29 1 34 35 0 35 30 1
		 35 36 0 36 31 1 36 37 0 37 32 1 6 5 1 37 6 0 41 83 1 83 84 1 84 40 1 82 44 1 42 81 1
		 81 82 1 82 83 1 84 85 1 85 38 1 85 86 1 86 39 1 8 7 1 68 69 1 86 87 1 87 12 1 70 71 1
		 46 11 1 56 27 1 47 4 1 24 48 1 21 49 1 26 50 1 19 51 1 16 52 1 45 89 1 89 81 1 88 89 1
		 43 88 1 87 88 1 15 67 1 11 68 1 46 69 1 14 70 1 0 71 1 73 60 1 60 61 0 61 72 1 61 62 0
		 62 74 1 62 63 0 63 75 1 63 64 0 64 76 1 64 65 0 65 77 1 65 57 0 57 78 1 57 58 0 58 79 1
		 58 59 0 59 80 1 59 60 0 26 82 1 81 19 1 21 83 1 20 84 1 22 85 1 27 86 1 56 87 1 55 88 1
		 54 89 1 67 90 1 68 91 1 90 91 0;
	setAttr ".ed[166:331]" 66 92 1 18 93 1 92 93 0 69 94 1 70 95 1 94 95 0 92 90 0
		 91 94 0 71 96 1 95 96 0 124 98 1 98 154 1 154 156 1 156 124 1 123 124 1 156 157 1
		 157 123 1 125 123 1 157 158 1 158 125 1 127 129 1 129 160 1 160 161 1 161 127 1 98 128 1
		 128 155 1 155 154 1 128 130 1 130 162 1 162 155 1 129 126 1 126 159 1 159 160 1 130 127 1
		 161 162 1 126 125 1 158 159 1 139 97 1 97 101 1 101 138 1 138 139 1 150 151 1 100 131 1
		 131 112 1 112 99 1 99 100 1 101 103 1 103 137 1 137 138 1 47 132 1 132 117 1 117 5 1
		 132 133 1 133 116 1 116 117 1 8 103 1 103 149 1 149 18 1 152 153 1 4 109 1 109 106 1
		 149 150 1 0 100 1 99 1 1 110 2 1 99 110 1 103 102 1 102 104 1 104 137 1 109 108 1
		 108 105 1 105 106 1 107 105 1 108 110 1 110 107 1 3 108 1 133 134 1 134 115 1 115 116 1
		 106 111 1 111 104 1 134 135 1 135 114 1 114 115 1 102 7 1 136 53 1 9 113 1 113 136 1
		 113 114 1 135 136 1 112 107 1 10 118 0 118 113 1 118 119 0 119 114 1 119 120 0 120 115 1
		 120 121 0 121 116 1 121 122 0 122 117 1 122 6 0 126 165 1 165 166 1 166 125 1 164 129 1
		 127 163 1 163 164 1 164 165 1 166 167 1 167 123 1 167 168 1 168 124 1 151 152 1 168 169 1
		 169 98 1 153 71 1 131 97 1 139 112 1 109 132 1 106 133 1 111 134 1 104 135 1 102 136 1
		 130 171 1 171 163 1 170 171 1 128 170 1 169 170 1 101 150 1 97 151 1 131 152 1 100 153 1
		 155 143 1 143 144 0 144 154 1 144 145 0 145 156 1 145 146 0 146 157 1 146 147 0 147 158 1
		 147 148 0 148 159 1 148 140 0 140 160 1 140 141 0 141 161 1 141 142 0 142 162 1 142 143 0
		 111 164 1 163 104 1 106 165 1 105 166 1 107 167 1 112 168 1 139 169 1 138 170 1 137 171 1
		 150 172 1 151 173 1 172 173 0 149 174 1 174 93 0 152 175 1;
	setAttr ".ed[332:336]" 153 176 1 175 176 0 174 172 0 173 175 0 176 96 0;
	setAttr -s 177 ".n";
	setAttr ".n[0:165]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20;
	setAttr ".n[166:176]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20;
	setAttr -s 158 -ch 632 ".fc[0:157]" -type "polyFaces" 
		f 4 0 1 2 3
		f 4 4 -4 5 6
		f 4 7 -7 8 9
		f 4 10 11 12 13
		f 4 14 15 16 -2
		f 4 17 18 19 -16
		f 4 20 21 22 -12
		f 4 23 -14 24 -19
		f 4 25 -10 26 -22
		f 4 27 28 29 30
		f 4 32 33 34 35
		f 4 36 37 38 -30
		f 4 39 40 41 42
		f 4 43 44 45 -42
		f 4 46 47 48 49
		f 4 51 121 -41 120
		f 4 52 122 -44 -122
		f 4 54 -36 55 56
		f 4 57 58 -56 59
		f 4 -38 60 61 62
		f 4 -53 63 64 65
		f 4 66 -65 67 68
		f 4 -52 69 70 -64
		f 4 -71 71 -58 -68
		f 4 72 73 74 -45
		f 4 75 123 -73 -123
		f 4 76 124 -78 -124
		f 4 77 78 79 -74
		f 4 81 80 -83 -126
		f 4 82 83 84 85
		f 4 -62 125 -88 -125
		f 4 -86 86 -79 87
		f 4 -69 -60 -35 88
		f 4 -85 89 90 91
		f 4 -92 92 93 -87
		f 4 -80 -94 94 95
		f 4 -75 -96 96 97
		f 4 -46 -98 98 99
		f 4 100 -43 -100 101
		f 4 102 103 104 -26
		f 4 105 -11 106 107
		f 4 -103 -21 -106 108
		f 4 -105 109 110 -8
		f 4 -111 111 112 -5
		f 4 -61 -47 113 -82
		f 4 -1 -113 115 116
		f 4 118 -28 119 -34
		f 4 126 127 -107 -24
		f 4 128 -127 -18 129
		f 4 -117 130 -130 -15
		f 4 131 -54 -48 -37
		f 4 132 -32 -132 -29
		f 4 133 -115 -133 -119
		f 4 134 -51 -134 -33
		f 4 -118 -135 -55 135
		f 4 -17 136 137 138
		f 4 -3 -139 139 140
		f 4 -6 -141 141 142
		f 4 -9 -143 143 144
		f 4 -27 -145 145 146
		f 4 -23 -147 147 148
		f 4 -13 -149 149 150
		f 4 -25 -151 151 152
		f 4 -20 -153 153 -137
		f 4 154 -108 155 -77
		f 4 156 -109 -155 -76
		f 4 -104 -157 -66 157
		f 4 -110 -158 -67 158
		f 4 -112 -159 -89 159
		f 4 -116 -160 -120 160
		f 4 -131 -161 -31 161
		f 4 -39 162 -129 -162
		f 4 -128 -163 -63 -156
		f 4 31 164 -166 -164
		f 4 -49 166 168 -168
		f 4 50 170 -172 -170
		f 4 53 163 -173 -167
		f 4 114 169 -174 -165
		f 4 117 174 -176 -171
		f 4 -180 -179 -178 -177
		f 4 -183 -182 179 -181
		f 4 -186 -185 182 -184
		f 4 -190 -189 -188 -187
		f 4 177 -193 -192 -191
		f 4 191 -196 -195 -194
		f 4 187 -199 -198 -197
		f 4 194 -201 189 -200
		f 4 197 -203 185 -202
		f 4 -207 -206 -205 -204
		f 4 -212 -211 -210 -209
		f 4 205 -215 -214 -213
		f 4 -218 -217 -216 -40
		f 4 216 -221 -220 -219
		f 4 -50 -224 -223 -222
		f 4 -121 215 -286 -226
		f 4 285 218 -287 -227
		f 4 -57 -230 211 -229
		f 4 -232 229 -59 -231
		f 4 -235 -234 -233 213
		f 4 -238 -237 -236 226
		f 4 -241 -240 236 -239
		f 4 235 -242 -70 225
		f 4 239 230 -72 241
		f 4 219 -245 -244 -243
		f 4 286 242 -288 -246
		f 4 287 247 -289 -247
		f 4 243 -250 -249 -248
		f 4 289 251 -81 -251
		f 4 -254 -253 -84 -252
		f 4 288 255 -290 233
		f 4 -256 248 -255 253
		f 4 -257 210 231 240
		f 4 -259 -258 -90 252
		f 4 254 -261 -260 258
		f 4 -263 -262 260 249
		f 4 -265 -264 262 244
		f 4 -267 -266 264 220
		f 4 -268 266 217 -101
		f 4 201 -271 -270 -269
		f 4 -274 -273 186 -272
		f 4 -275 271 196 268
		f 4 183 -277 -276 270
		f 4 180 -279 -278 276
		f 4 250 -114 221 232
		f 4 -282 -281 278 176
		f 4 209 -285 203 -284
		f 4 199 272 -292 -291
		f 4 -294 193 290 -293
		f 4 190 293 -295 281
		f 4 212 222 227 -296
		f 4 204 295 207 -297
		f 4 283 296 279 -298
		f 4 208 297 224 -299
		f 4 -136 228 298 282
		f 4 -302 -301 -300 192
		f 4 -304 -303 301 178
		f 4 -306 -305 303 181
		f 4 -308 -307 305 184
		f 4 -310 -309 307 202
		f 4 -312 -311 309 198
		f 4 -314 -313 311 188
		f 4 -316 -315 313 200
		f 4 299 -317 315 195
		f 4 246 -319 273 -318
		f 4 245 317 274 -320
		f 4 -321 237 319 269
		f 4 -322 238 320 275
		f 4 -323 256 321 277
		f 4 -324 284 322 280
		f 4 -325 206 323 294
		f 4 324 292 -326 214
		f 4 318 234 325 291
		f 4 326 328 -328 -208
		f 4 167 -331 -330 223
		f 4 331 333 -333 -225
		f 4 329 334 -327 -228
		f 4 327 335 -332 -280
		f 4 332 336 -175 -283;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vs" 6;
	setAttr ".bw" 6;
createNode transform -n "mocap_head_PLY" -p "mocap_geometry_GRP";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023BB";
	setAttr ".ove" yes;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode mesh -n "mocap_head_PLYShape" -p "mocap_head_PLY";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023BC";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ugsdt" no;
	setAttr ".vs" 6;
	setAttr ".bw" 6;
	setAttr ".dr" 1;
	setAttr ".vcs" 2;
createNode mesh -n "mocap_head_PLYShapeOrig" -p "mocap_head_PLY";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023BD";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ugsdt" no;
	setAttr -s 376 ".vt";
	setAttr ".vt[0:165]"  0.17860398 15.8424654 0.99189347 0.31959265 15.85364056 0.95611453
		 0.4785721 15.8586359 0.95504642 0.15842785 15.16850758 1.067788601 0.13951732 15.16366005 1.089890957
		 0.057920597 15.17424107 1.133196 0 15.17750645 1.14201307 0 15.18045235 1.13905656
		 0.086628608 15.17675877 1.12414014 0.22551005 15.98112583 1.09150207 0.16517183 16.19608498 1.13543582
		 0 16.20275307 1.15057874 0.33914378 16.0075778961 1.054807663 0.46470922 15.99724293 1.0096960068
		 0.50699157 15.71280098 0.98647487 0.24116276 15.71474171 1.047599196 0.35398182 16.16866112 1.050376892
		 0.5963071 16.10088158 0.91929144 0.61085856 15.88947105 0.80797869 0.62860221 15.5792017 0.89301741
		 0.43890378 15.453475 1.0366292 0.19731838 15.57067871 1.073022246 0.088434614 15.78159714 1.090697169
		 0 15.83289051 1.14525604 0.27808911 15.33707142 1.06459856 0.17409548 15.28179836 1.10833311
		 0.15842724 15.44126225 1.085579157 0.18608142 15.48498631 1.18807125 0.2407857 15.17835522 1.075217485
		 0.21296035 15.099092484 1.073673368 0.11779466 15.055054665 1.12225246 0.15550169 14.99529457 1.10535419
		 0.28078458 15.070837975 1.043411255 0.3253752 15.1937561 1.032478929 0.48192704 15.22561455 0.94006014
		 0.38965148 15.03457737 0.9478848 0 14.83664703 1.14471006 0.23303996 14.88244247 1.069028735
		 0.64053929 15.30577374 0.73684478 0 15.53022671 1.3727845 0.067874961 15.5348587 1.34796023
		 0 15.41522598 1.33136892 0.051278885 15.4134655 1.3245666 0.10776817 15.37937069 1.14158237
		 0.13618347 15.41088963 1.22887778 0.03738961 15.37994576 1.1947068 0 15.29377842 1.19284344
		 0.061404008 15.30167961 1.18067372 0 15.23866177 1.19920945 0.058975916 15.24046516 1.17709541
		 0.14922643 15.2170639 1.12421322 0.1957753 15.1686306 1.080786705 0.18078583 15.12677574 1.088382363
		 0.10220204 15.1075201 1.15142548 0.51775342 15.003569603 0.74513656 0.27462664 14.80401134 0.88107938
		 0 14.73537827 1.020381808 0.6790337 15.39845085 0.49654955 0.70192289 15.62759972 0.53298199
		 0.56654441 15.02161026 0.47585303 0.27751923 14.75868893 0.63715631 0 14.6691761 0.74145055
		 0.68560362 15.98124218 0.58019197 0.66860831 16.23371696 0.77536815 0.38082322 16.35014534 0.92087489
		 0.17294021 16.38653564 1.011094332 0 16.39048004 1.065297842 0 15.20560265 1.18222272
		 0.04686692 15.2019577 1.15333569 0.13161319 15.18604565 1.11072028 0.17721471 15.16024208 1.079065204
		 0.16866532 15.14735603 1.084043503 0.09316773 15.14975357 1.14258659 0 15.050621033 1.14226508
		 0 15.0036659241 1.13512146 0 15.1072216 1.18124747 0 15.15706062 1.17849851 0 15.37854958 1.19240522
		 0.8079083 15.94020271 0.0095957369 0.82168758 16.12108612 -0.12407639 0.7980755 15.80189514 -0.093749821
		 0.78710943 15.86328125 -0.24662626 0.72303855 15.58985996 -0.10618497 0.68075842 15.593256 -0.27296618
		 0.64374334 15.32105827 0.057951756 0.58319068 15.22407627 -0.12483446 0.81182897 16.22948837 0.099598892
		 0.82037932 15.97938728 0.14817905 0.76395023 16.2303791 0.33602071 0.78477031 15.90281391 0.33894119
		 0.70295912 16.21076775 0.50339425 0.51641572 16.75997162 0.4726066 0.24185464 16.87822151 0.53195685
		 0.70221472 16.51927948 0.3922303 0.19299807 16.62604904 0.83519912 0.76211739 16.552742 0.07073684
		 0.56272143 16.84010315 0.056170914 0.28623718 16.96923065 0.028922923 0.74126768 16.42868042 -0.28991401
		 0.57015008 16.66690254 -0.4253881 0.28788146 16.84263992 -0.53246063 0.70209324 16.0650177 -0.51438427
		 0.59136766 16.20676422 -0.78379601 0.31581017 16.31115341 -0.95480096 0.59411865 15.6436882 -0.52530056
		 0.49102801 15.64424229 -0.78419036 0.25384921 15.6535902 -0.94584072 0.52319336 15.23752689 -0.3929204
		 0.44214976 15.18689346 -0.64488643 0.21923266 15.17946434 -0.74595082 0.44044188 16.55956078 0.74568129
		 0.62533271 16.39934921 0.61474472 -1.582276e-06 16.65095139 0.87476176 -0.00023318906 16.90188026 0.53607881
		 0.00099003292 17.020820618 0.033861116 -0.00043472848 16.87083435 -0.54233855 -0.00093355501 16.34057999 -0.97926688
		 4.6422476e-05 15.6586895 -0.96049792 -5.4608627e-06 15.18501472 -0.73967928 0.71815819 15.66238022 0.38474211
		 0.69360065 15.47969246 0.38341704 0.69478643 15.34972382 0.33787587 0.64674157 15.25817108 0.2156121
		 0.43872461 14.4730072 0.16847616 0.5455547 14.55601406 -0.0071667172 0.46396321 14.85240364 0.25898516
		 0.23217778 14.6463623 0.43146542 0 14.57827759 0.58350945 0.23849294 14.33320427 0.32136998
		 0.51487803 14.91554356 0.045264471 0.6412189 14.18772507 -0.64519602 0.88733935 14.1090517 -0.68760002
		 0.50073344 14.90784836 -0.11935493 0.46274066 14.86130047 -0.28643847 0.32267883 14.81755924 -0.42909881
		 0.15381792 14.80858612 -0.51800895 0.60432965 14.5609045 -0.17519546 0.58460325 14.48335838 -0.41731459
		 0.37783551 14.48469353 -0.50639695 0.18402918 14.45170879 -0.56371033 0 14.18303871 0.42207915
		 0 13.84415245 0.49616653 0.32137549 13.97974396 0.37180865 0.6354785 14.05388546 0.22140926
		 0.74662948 14.16818142 0.0057811998 0.82911581 14.24878407 -0.20334405 0.86190242 14.23522663 -0.47421956
		 0.34406471 13.67170525 0.60307115 0.70265073 13.75529099 0.47544643 0 13.64371586 0.67445552
		 0.99538136 13.79846001 0.35109094 1.036902666 13.89881611 0.18351668 1.11157608 13.97459507 0.010767082
		 0.41613567 13.85862255 -0.79466891 0.71290803 13.95421314 -0.80141461 0.17363 14.13306999 -0.67403698
		 0.11861128 13.81047058 -0.8250668 0.4116503 14.16091633 -0.63210595 1.17954433 14.071372986 -0.20431913
		 0.87007803 13.96028709 -0.8417291 0 13.41935825 0.8371945 0.36338627 13.42289734 0.78117561
		 0.74654275 13.50800705 0.67765367 1.18348575 13.65719604 0.4561587 1.42019713 13.86865997 0.13819921
		 1.47951448 13.93435478 -0.0072924234;
	setAttr ".vt[166:331]" 1.52671468 14.028939247 -0.16346684 1.18697274 14.057911873 -0.70434964
		 1.20674837 14.11276627 -0.49543515 1.53661847 14.068159103 -0.48403496 1.39928937 13.9780159 -0.81444573
		 1.4010936e-06 14.82733727 -0.54788607 0 14.39893913 -0.62807459 0 14.12153435 -0.70159709
		 0 13.81386757 -0.8295424 0.93535519 15.93015766 0.0062773973 0.97458625 15.79692364 -0.15526357
		 0.9354251 15.58281612 -0.15331464 0.81582475 15.37968826 0.034126431 0.89510542 15.89622974 0.14986208
		 0.80543101 15.80005932 0.25215265 0.73407871 15.65454102 0.30186382 0.73890215 15.45597172 0.26548535
		 0.70474923 15.5337553 0.30548057 0.77484494 15.40199471 0.18020746 0.86837918 15.78215599 0.04017996
		 0.90859449 15.72362328 -0.071274184 0.85949582 15.59830379 -0.078851849 0.81174648 15.47599888 0.020032413
		 0.84436333 15.77533245 0.14452738 0.78542864 15.74994469 0.21571577 0.7255047 15.65324879 0.24000371
		 0.69417679 15.53995037 0.20044377 0.69987077 15.5714035 0.25313929 0.69939369 15.50083733 0.11645028
		 0.69612396 15.65537834 0.038468599 0.72465706 15.65165806 0.15306592 0.37282583 15.69013309 1.024118423
		 -0.17860398 15.8424654 0.99189347 -0.31959268 15.85364056 0.95611453 -0.47857213 15.8586359 0.95504642
		 -0.15842785 15.16850758 1.067788601 -0.13951734 15.16366005 1.089890957 -0.02606087 15.17424107 1.133196
		 -0.086628601 15.17675877 1.12414014 -0.22551006 15.98112583 1.09150207 -0.16517183 16.19608498 1.13543582
		 -0.33914375 16.0075778961 1.054807663 -0.46470925 15.99724293 1.0096960068 -0.50699157 15.71280098 0.98647487
		 -0.24116278 15.71474171 1.047599196 -0.35398182 16.16866112 1.050376892 -0.59630716 16.10088158 0.91929144
		 -0.6108585 15.88947105 0.80797869 -0.62860221 15.5792017 0.89301741 -0.43890375 15.453475 1.0366292
		 -0.19731838 15.57067871 1.073022246 -0.088434622 15.78159714 1.090697169 -0.27808914 15.33707142 1.06459856
		 -0.1740955 15.28179836 1.10833311 -0.15842724 15.44126225 1.085579157 -0.18608144 15.48498631 1.18807125
		 -0.24078569 15.17835522 1.075217485 -0.21296033 15.099092484 1.073673368 -0.11779466 15.055054665 1.12225246
		 -0.15550168 14.99529457 1.10535419 -0.28078455 15.070837975 1.043411255 -0.3253752 15.1937561 1.032478929
		 -0.48192704 15.22561455 0.94006014 -0.38965145 15.03457737 0.9478848 -0.23303995 14.88244247 1.069028735
		 -0.64053929 15.30577374 0.73684478 -0.067874968 15.5348587 1.34796023 -0.051278885 15.4134655 1.3245666
		 -0.10776817 15.37937069 1.14158237 -0.13618347 15.41088963 1.22887778 -0.03738961 15.37994576 1.1947068
		 -0.061404005 15.30167961 1.18067372 -0.058975916 15.24046516 1.17709541 -0.14922641 15.2170639 1.12421322
		 -0.1957753 15.1686306 1.080786705 -0.18078583 15.12677574 1.088382363 -0.10220204 15.1075201 1.15142548
		 -0.51775342 15.003569603 0.74513656 -0.27462661 14.80401134 0.88107938 -0.67903376 15.39845085 0.49654955
		 -0.70192283 15.62759972 0.53298199 -0.56654441 15.02161026 0.47585303 -0.27751926 14.75868893 0.63715631
		 -0.68560362 15.98124218 0.58019197 -0.66860825 16.23371696 0.77536815 -0.38082319 16.35014534 0.92087489
		 -0.17294021 16.38653564 1.011094332 -0.04686692 15.2019577 1.15333569 -0.13161321 15.18604565 1.11072028
		 -0.1772147 15.16024208 1.079065204 -0.16866532 15.14735603 1.084043503 -0.093167722 15.14975357 1.14258659
		 -0.8079083 15.94020271 0.0095957369 -0.82168764 16.12108612 -0.12407639 -0.7980755 15.80189514 -0.093749821
		 -0.78710943 15.86328125 -0.24662626 -0.72303855 15.58985996 -0.10618497 -0.68075848 15.593256 -0.27296618
		 -0.6437434 15.32105827 0.057951756 -0.58319062 15.22407627 -0.12483446 -0.81182891 16.22948837 0.099598892
		 -0.82037932 15.97938728 0.14817905 -0.76395029 16.2303791 0.33602071 -0.78477031 15.90281391 0.33894119
		 -0.70295912 16.21076775 0.50339425 -0.51951283 16.76095581 0.473829 -0.24498999 16.87585449 0.52701062
		 -0.70284289 16.51952934 0.39247206 -0.19308721 16.62496948 0.83382934 -0.76211739 16.552742 0.07073684
		 -0.56942725 16.84514999 0.055471905 -0.29587457 17.0055007935 0.030380763 -0.74061805 16.4286499 -0.28981286
		 -0.56718981 16.66456795 -0.42390883 -0.29436415 16.83636475 -0.53092194 -0.70041537 16.065229416 -0.51391768
		 -0.58462548 16.20673752 -0.78083557 -0.31709301 16.30955696 -0.95131773 -0.58966875 15.64554977 -0.5230903
		 -0.48645213 15.6456604 -0.78065091 -0.25587723 15.65299892 -0.9484545 -0.51726413 15.23980141 -0.39016443
		 -0.43841738 15.18983841 -0.64063871 -0.22106864 15.17694378 -0.75084507 -0.44063643 16.55972862 0.74583185
		 -0.62533271 16.39934921 0.61474472 -0.71815819 15.66238022 0.38474211 -0.69360059 15.47969246 0.38341704
		 -0.69478643 15.34972382 0.33787587 -0.64674157 15.25817108 0.2156121 -0.45833549 14.48841572 0.16847616
		 -0.56994766 14.57518005 -0.0071667172 -0.46396318 14.85240364 0.25898516 -0.23217779 14.6463623 0.43146542
		 -0.24112064 14.33526897 0.32136998 -0.51487803 14.91554356 0.045264471 -0.68115991 14.21910763 -0.64519602
		 -0.93256217 14.1445837 -0.68760002 -0.5010128 14.9080677 -0.11935493 -0.46355906 14.86194324 -0.28643847
		 -0.32233843 14.81750774 -0.42856884 -0.15350978 14.80842495 -0.51750231 -0.63418615 14.58436298 -0.17519546
		 -0.6146006 14.50692749 -0.41731459 -0.38674253 14.49169159 -0.50639695 -0.18402918 14.45170879 -0.56371033
		 -0.32400319 13.98180866 0.37180865 -0.67767632 14.087040901 0.22140926 -0.80657995 14.2152853 0.0057811998
		 -0.88906634 14.29588795 -0.20334405 -0.92185289 14.28233051 -0.47421956 -0.34406468 13.67170525 0.60307115
		 -0.70533997 13.75740433 0.47544643 -1.004714489 13.80579281 0.35109094 -1.061410666 13.9180727 0.18351668
		 -1.13989556 13.9968462 0.010767082 -0.41613567 13.85862255 -0.79466891 -0.72846365 13.96643543 -0.80141461
		 -0.17362998 14.13306999 -0.67403698 -0.11861129 13.81047058 -0.8250668 -0.42272997 14.16962147 -0.63210595
		 -1.21030295 14.095541 -0.20431913 -0.88809776 13.97444534 -0.8417291 -0.36338627 13.42289734 0.78117561
		 -0.74654275 13.50800705 0.67765367 -1.18348575 13.65719604 0.4561587;
	setAttr ".vt[332:375]" -1.42066085 13.86902428 0.13819921 -1.4805423 13.93516254 -0.0072924234
		 -1.52837813 14.030246735 -0.16346684 -1.21228862 14.077802658 -0.70434964 -1.24096537 14.1396513 -0.49543515
		 -1.54013216 14.070919991 -0.48403496 -1.40215123 13.98026466 -0.81444573 -0.93535513 15.93015766 0.0062773973
		 -0.97458625 15.79692364 -0.15526357 -0.9354251 15.58281612 -0.15331464 -0.81582469 15.37968826 0.034126431
		 -0.89510542 15.89622974 0.14986208 -0.80543107 15.80005932 0.25215265 -0.73407871 15.65454102 0.30186382
		 -0.73890215 15.45597172 0.26548535 -0.70474923 15.5337553 0.30548057 -0.77484488 15.40199471 0.18020746
		 -0.86837912 15.78215599 0.04017996 -0.90859455 15.72362328 -0.071274184 -0.85949588 15.59830379 -0.078851849
		 -0.81174648 15.47599888 0.020032413 -0.84436333 15.77533245 0.14452738 -0.78542864 15.74994469 0.21571577
		 -0.7255047 15.65324879 0.24000371 -0.69417679 15.53995037 0.20044377 -0.69987077 15.5714035 0.25313929
		 -0.69939375 15.50083733 0.11645028 -0.69612396 15.65537834 0.038468599 -0.72465706 15.65165806 0.15306592
		 -0.3728258 15.69013309 1.024118423 0 16.39048004 2.17934465 0 16.20275307 2.28214955
		 0.16517183 16.19608498 2.26700664 0.17294021 16.38653564 2.14266515 0.35398182 16.16866112 2.18194771
		 0.38082322 16.35014534 2.05244565 0.51747662 16.10088158 2.050862312 0.58021975 16.23371696 1.90693903
		 -0.17294021 16.38653564 2.14266515 -0.16517183 16.19608498 2.26700664 -0.38082319 16.35014534 2.05244565
		 -0.35398182 16.16866112 2.18194771 -0.58021969 16.23371696 1.90693903 -0.51747662 16.10088158 2.050862312;
	setAttr -s 736 ".ed";
	setAttr ".ed[0:165]"  0 1 1 1 2 1 3 4 0 4 5 0 5 6 0 7 8 0 8 3 0 67 6 1 9 10 1
		 10 11 1 9 12 1 12 13 1 14 197 1 12 16 1 16 10 1 13 17 1 17 16 1 2 18 1 18 17 1 14 19 1
		 19 18 1 20 19 1 15 21 1 0 22 1 22 21 1 23 22 1 11 23 1 20 34 1 24 25 1 25 28 1 27 26 1
		 47 25 1 29 28 1 30 29 1 73 30 1 31 30 1 31 32 1 32 29 1 32 33 1 33 28 1 33 24 1 35 34 1
		 37 36 1 35 37 1 34 38 1 38 19 1 23 39 1 39 40 1 39 41 1 41 42 1 42 40 1 26 43 1 27 44 1
		 44 43 1 42 44 1 45 43 1 47 49 1 49 48 1 50 49 1 51 50 1 52 51 1 53 52 1 35 54 1 54 38 1
		 37 55 1 55 54 1 36 56 1 38 57 1 57 58 1 59 57 1 54 59 1 55 60 1 60 59 1 56 61 1 61 60 1
		 58 62 1 62 18 1 62 63 1 63 17 1 63 64 1 64 65 1 65 66 1 5 68 1 68 67 1 4 69 1 69 68 1
		 3 70 1 70 69 1 3 71 1 71 70 1 8 72 1 72 71 1 73 74 1 74 31 1 75 73 1 76 75 1 75 53 1
		 7 76 1 76 72 1 56 55 1 21 27 1 22 40 1 74 36 1 0 15 1 49 68 1 48 67 1 53 72 1 52 71 1
		 51 70 1 50 69 1 2 14 1 0 9 1 1 12 1 2 13 1 30 53 1 29 52 1 28 51 1 25 50 1 20 24 1
		 33 34 1 32 35 1 31 37 1 24 26 1 45 47 1 47 46 1 45 77 1 46 48 1 45 42 1 78 79 1 79 86 1
		 78 80 1 80 81 1 81 79 1 80 82 1 82 83 1 83 81 1 82 84 1 84 85 1 85 83 1 86 87 1 87 78 1
		 88 89 1 89 87 1 88 90 1 90 62 1 62 89 1 86 88 1 92 91 1 63 111 1 92 94 1 93 91 1
		 88 93 1 111 90 1 94 65 1 95 86 1 96 95 1 97 96 1 79 98 1 98 95 1 98 99 1 99 96 1
		 99 100 1 100 97 1 81 101 1 101 98 1 101 102 1;
	setAttr ".ed[166:331]" 102 99 1 102 103 1 103 100 1 83 104 1 104 101 1 104 105 1
		 105 102 1 105 106 1 106 103 1 85 107 1 107 104 1 107 108 1 108 105 1 108 109 1 109 106 1
		 94 110 1 110 91 1 110 111 1 111 93 1 110 64 1 95 93 1 96 91 1 97 92 1 94 112 1 112 66 1
		 92 113 1 113 112 1 97 114 1 114 113 1 100 115 1 115 114 1 116 115 1 103 116 1 117 116 1
		 106 117 1 118 117 1 109 118 1 58 119 1 119 89 1 120 57 1 59 121 1 121 120 1 122 121 1
		 84 122 1 124 123 1 59 125 1 125 122 1 60 126 1 126 125 1 61 127 1 127 126 1 123 128 1
		 129 125 1 130 131 1 131 159 1 129 84 1 129 132 1 132 85 1 132 133 1 133 107 1 133 134 1
		 134 108 1 134 135 1 135 109 1 136 124 1 137 138 1 138 139 1 139 135 1 127 140 1 140 128 1
		 128 126 1 123 125 1 124 129 1 136 132 1 137 133 1 138 134 1 140 141 1 141 142 1 128 142 1
		 142 143 1 143 123 1 143 144 1 144 124 1 144 145 1 145 136 1 145 146 1 146 137 1 130 137 1
		 146 131 1 142 147 1 147 148 1 141 149 1 149 147 1 148 150 1 150 151 1 148 143 1 151 143 1
		 151 152 1 152 144 1 154 153 0 130 154 1 155 139 1 153 156 0 156 155 1 155 157 1 157 153 1
		 157 130 1 145 158 1 152 158 1 138 157 1 159 154 0 170 159 0 149 160 1 160 161 0 161 147 1
		 161 162 0 162 148 1 162 163 0 163 150 1 163 164 0 164 151 1 164 165 0 165 152 1 165 166 0
		 166 158 1 167 131 1 146 168 1 168 167 1 158 168 1 166 169 0 169 168 1 169 170 0 170 167 1
		 171 118 1 135 171 1 172 171 1 139 172 1 173 172 1 155 173 1 174 173 1 156 174 0 41 77 1
		 22 10 1 40 27 1 119 120 1 78 175 1 175 176 1 80 176 1 176 177 1 82 177 1 177 178 1
		 84 178 1 87 179 1 179 175 1 89 180 1 180 179 1 119 181 1 181 180 1 121 182 1 120 183 1
		 182 183 1 122 184 1 184 182 1 178 184 1 181 183 1 175 185 1;
	setAttr ".ed[332:497]" 176 186 1 185 186 1 177 187 1 186 187 1 178 188 1 187 188 1
		 179 189 1 189 185 1 180 190 1 190 189 1 181 191 1 191 190 1 182 192 1 183 193 1 192 193 1
		 184 194 1 194 192 1 188 194 1 191 193 1 189 196 1 185 195 1 58 19 1 195 194 1 187 195 1
		 196 192 1 195 196 1 196 191 1 43 25 1 21 20 1 197 15 1 1 197 1 26 21 1 20 197 1 136 137 1
		 77 46 1 198 199 1 199 200 1 201 202 0 202 203 0 203 6 0 7 204 0 204 201 0 205 206 1
		 206 11 1 205 207 1 207 208 1 209 361 1 207 211 1 211 206 1 208 212 1 212 211 1 200 213 1
		 213 212 1 209 214 1 214 213 1 215 214 1 210 216 1 198 217 1 217 216 1 23 217 1 215 228 1
		 218 219 1 219 222 1 221 220 1 237 219 1 223 222 1 224 223 1 73 224 1 225 224 1 225 226 1
		 226 223 1 226 227 1 227 222 1 227 218 1 229 228 1 230 36 1 229 230 1 228 231 1 231 214 1
		 39 232 1 41 233 1 233 232 1 220 234 1 221 235 1 235 234 1 233 235 1 236 234 1 237 238 1
		 238 48 1 239 238 1 240 239 1 241 240 1 242 241 1 229 243 1 243 231 1 230 244 1 244 243 1
		 231 245 1 245 246 1 247 245 1 243 247 1 244 248 1 248 247 1 61 248 1 246 249 1 249 213 1
		 249 250 1 250 212 1 250 251 1 251 252 1 252 66 1 203 253 1 253 67 1 202 254 1 254 253 1
		 201 255 1 255 254 1 201 256 1 256 255 1 204 257 1 257 256 1 74 225 1 75 242 1 76 257 1
		 56 244 1 216 221 1 217 232 1 198 210 1 238 253 1 242 257 1 241 256 1 240 255 1 239 254 1
		 200 209 1 198 205 1 199 207 1 200 208 1 224 242 1 223 241 1 222 240 1 219 239 1 215 218 1
		 227 228 1 226 229 1 225 230 1 218 220 1 236 237 1 237 46 1 236 77 1 236 233 1 258 259 1
		 259 266 1 258 260 1 260 261 1 261 259 1 260 262 1 262 263 1 263 261 1 262 264 1 264 265 1
		 265 263 1 266 267 1 267 258 1 268 269 1 269 267 1 268 270 1;
	setAttr ".ed[498:663]" 270 249 1 249 269 1 266 268 1 272 271 1 250 291 1 272 274 1
		 273 271 1 268 273 1 291 270 1 274 252 1 275 266 1 276 275 1 277 276 1 259 278 1 278 275 1
		 278 279 1 279 276 1 279 280 1 280 277 1 261 281 1 281 278 1 281 282 1 282 279 1 282 283 1
		 283 280 1 263 284 1 284 281 1 284 285 1 285 282 1 285 286 1 286 283 1 265 287 1 287 284 1
		 287 288 1 288 285 1 288 289 1 289 286 1 274 290 1 290 271 1 290 291 1 291 273 1 290 251 1
		 275 273 1 276 271 1 277 272 1 274 112 1 272 113 1 277 114 1 280 115 1 283 116 1 286 117 1
		 289 118 1 246 292 1 292 269 1 293 245 1 247 294 1 294 293 1 295 294 1 264 295 1 297 296 1
		 247 298 1 298 295 1 248 299 1 299 298 1 127 299 1 296 300 1 301 298 1 302 303 1 303 328 1
		 301 264 1 301 304 1 304 265 1 304 305 1 305 287 1 305 306 1 306 288 1 306 307 1 307 289 1
		 308 297 1 309 310 1 310 311 1 311 307 1 140 300 1 300 299 1 296 298 1 297 301 1 308 304 1
		 309 305 1 310 306 1 141 312 1 300 312 1 312 313 1 313 296 1 313 314 1 314 297 1 314 315 1
		 315 308 1 315 316 1 316 309 1 302 309 1 316 303 1 312 317 1 317 318 1 149 317 1 318 319 1
		 319 320 1 318 313 1 320 313 1 320 321 1 321 314 1 323 322 0 302 323 1 324 311 1 322 325 0
		 325 324 1 324 326 1 326 322 1 326 302 1 315 327 1 321 327 1 310 326 1 328 323 0 338 328 0
		 160 329 0 329 317 1 329 330 0 330 318 1 330 331 0 331 319 1 331 332 0 332 320 1 332 333 0
		 333 321 1 333 334 0 334 327 1 335 303 1 316 336 1 336 335 1 327 336 1 334 337 0 337 336 1
		 337 338 0 338 335 1 307 171 1 311 172 1 324 173 1 325 174 0 217 206 1 232 221 1 292 293 1
		 258 339 1 339 340 1 260 340 1 340 341 1 262 341 1 341 342 1 264 342 1 267 343 1 343 339 1
		 269 344 1 344 343 1 292 345 1 345 344 1 294 346 1 293 347 1 346 347 1;
	setAttr ".ed[664:735]" 295 348 1 348 346 1 342 348 1 345 347 1 339 349 1 340 350 1
		 349 350 1 341 351 1 350 351 1 342 352 1 351 352 1 343 353 1 353 349 1 344 354 1 354 353 1
		 345 355 1 355 354 1 346 356 1 347 357 1 356 357 1 348 358 1 358 356 1 352 358 1 355 357 1
		 353 360 1 349 359 1 246 214 1 359 358 1 351 359 1 360 356 1 359 360 1 360 355 1 234 219 1
		 216 215 1 361 210 1 199 361 1 220 216 1 215 361 1 308 309 1 66 362 1 11 363 1 362 363 1
		 10 364 1 364 363 1 65 365 1 365 364 1 365 362 1 16 366 1 366 364 1 64 367 1 367 366 1
		 367 365 1 17 368 1 368 366 1 63 369 1 369 368 1 369 367 1 252 370 1 370 362 1 206 371 1
		 370 371 1 371 363 1 251 372 1 372 370 1 211 373 1 372 373 1 373 371 1 250 374 1 374 372 1
		 212 375 1 374 375 1 375 373 1;
	setAttr -s 376 ".n";
	setAttr ".n[0:165]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20;
	setAttr ".n[166:331]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20;
	setAttr ".n[332:375]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20;
	setAttr -s 360 -ch 1436 ".fc[0:359]" -type "polyFaces" 
		f 4 7 -5 82 83
		f 4 -83 -4 84 85
		f 4 -85 -3 86 87
		f 3 -87 88 89
		f 4 -89 -7 90 91
		f 4 -91 -6 97 98
		f 4 -12 -113 1 113
		f 4 362 -13 -111 -2
		f 4 8 -309 -24 111
		f 4 9 26 25 308
		f 4 -9 10 13 14
		f 4 -14 11 15 16
		f 4 -16 -114 17 18
		f 4 -18 110 19 20
		f 4 361 22 360 364
		f 4 -104 23 24 -23
		f 4 705 -708 -710 710
		f 4 -713 -715 715 709
		f 4 -718 -720 720 714
		f 4 -19 -77 77 78
		f 4 353 -46 67 68
		f 4 -22 27 44 45
		f 4 -28 118 -41 119
		f 4 28 29 -40 40
		f 4 -29 122 51 359
		f 3 363 100 30
		f 4 -101 -25 101 309
		f 4 -26 46 47 -102
		f 4 -52 -31 52 53
		f 4 -59 -118 -32 56
		f 4 -60 -117 -30 117
		f 4 -61 -116 32 116
		f 4 -62 -115 33 115
		f 4 92 93 35 -35
		f 4 -36 36 37 -34
		f 4 -38 38 39 -33
		f 4 41 -120 -39 120
		f 4 -44 -121 -37 121
		f 4 -43 -122 -94 102
		f 4 -65 42 66 99
		f 4 -63 43 64 65
		f 4 -45 -42 62 63
		f 4 -48 48 49 50
		f 4 127 -50 307 -126
		f 4 -310 -51 54 -53
		f 4 57 105 -84 -105
		f 4 -86 -110 58 104
		f 4 -88 -109 59 109
		f 4 -90 -108 60 108
		f 4 -92 -107 61 107
		f 4 -72 -100 73 74
		f 4 -71 -66 71 72
		f 4 69 -68 -64 70
		f 4 -97 94 34 114
		f 4 -99 95 96 106
		f 4 -11 -112 0 112
		f 4 126 -58 -57 124
		f 4 128 129 139 140
		f 4 -129 130 131 132
		f 4 -132 133 134 135
		f 4 -135 136 137 138
		f 4 141 142 -140 146
		f 4 -142 143 144 145
		f 4 147 -188 -157 188
		f 4 -149 -78 -145 -153
		f 4 -80 148 -184 185
		f 4 149 181 182 -148
		f 4 -183 183 184 150
		f 4 152 -144 151 -185
		f 4 -151 -187 -156 187
		f 4 -152 -147 -155 186
		f 4 153 -81 -186 -182
		f 4 -130 157 158 154
		f 4 -159 159 160 155
		f 4 -161 161 162 156
		f 4 -158 -133 163 164
		f 4 -160 -165 165 166
		f 4 -162 -167 167 168
		f 4 -164 -136 169 170
		f 4 -166 -171 171 172
		f 4 -168 -173 173 174
		f 4 -174 -179 179 180
		f 4 -172 -177 177 178
		f 4 -170 -139 175 176
		f 4 -82 -154 189 190
		f 4 -190 -150 191 192
		f 4 -192 -189 193 194
		f 4 -194 -163 195 196
		f 4 197 -196 -169 198
		f 4 199 -199 -175 200
		f 4 201 -201 -181 202
		f 4 -146 -76 203 204
		f 4 205 -70 206 207
		f 4 208 -207 211 212
		f 4 209 -213 -219 221
		f 4 -138 -222 222 223
		f 4 210 -247 247 248
		f 4 -212 -73 213 214
		f 4 -214 -75 215 216
		f 4 217 244 245 246
		f 4 -236 242 243 -245
		f 4 -217 234 235 236
		f 4 -215 -237 -218 237
		f 4 218 -238 -211 238
		f 4 219 220 276 -267
		f 4 -176 -224 224 225
		f 4 -178 -226 226 227
		f 4 -180 -228 228 229
		f 4 -223 -239 -231 239
		f 4 230 -249 249 250
		f 4 365 240 -225 -240
		f 4 231 241 -227 -241
		f 4 232 233 -229 -242
		f 4 -220 253 -253 254
		f 4 -256 -244 257 258
		f 4 261 -246 255 256
		f 4 -262 259 260 262
		f 4 -261 -285 285 286
		f 4 -248 -263 263 264
		f 4 -264 -287 287 288
		f 4 -250 -265 274 -274
		f 4 -252 273 294 -293
		f 4 266 265 -272 272
		f 4 -271 267 -233 275
		f 4 270 271 268 269
		f 4 -254 -273 -276 -232
		f 4 -275 -289 289 290
		f 4 -295 -291 295 296
		f 4 -257 -281 281 282
		f 4 -259 278 279 280
		f 4 -260 -283 283 284
		f 4 291 -255 292 293
		f 4 -294 -297 297 298
		f 4 277 -221 -292 -299
		f 4 299 -203 -230 300
		f 4 301 -301 -234 302
		f 4 303 -303 -268 304
		f 4 305 -305 -270 306
		f 4 -204 -69 -206 -311
		f 4 -314 -131 311 312
		f 4 -316 -134 313 314
		f 4 -318 -137 315 316
		f 4 -141 318 319 -312
		f 4 -143 320 321 -319
		f 4 -205 322 323 -321
		f 4 -208 324 326 -326
		f 4 -209 327 328 -325
		f 4 -210 317 329 -328
		f 4 310 325 -331 -323
		f 4 333 -333 -313 331
		f 4 335 -335 -315 332
		f 4 337 -337 -317 334
		f 4 -320 338 339 -332
		f 4 -322 340 341 -339
		f 4 -324 342 343 -341
		f 4 -327 344 346 -346
		f 4 -329 347 348 -345
		f 4 -330 336 349 -348
		f 4 330 345 -351 -343
		f 4 354 -350 -338 355
		f 4 -357 358 350 -347
		f 4 -355 357 356 -349
		f 4 -21 -354 75 76
		f 4 352 -356 -336 -334
		f 4 -358 -353 -340 351
		f 4 -359 -352 -342 -344
		f 4 31 -360 -56 123
		f 4 -54 -55 -128 55
		f 4 -362 -363 -1 103
		f 4 -364 -123 -119 -361
		f 4 12 -365 21 -20
		f 4 -366 -251 251 252
		f 4 125 366 -125 -124
		f 4 -445 -444 371 -8
		f 4 -447 -446 370 443
		f 4 -449 -448 369 445
		f 3 -451 -450 447
		f 4 -453 -452 373 449
		f 4 -456 -98 372 451
		f 4 -469 -369 467 377
		f 4 368 465 378 -700
		f 4 -467 389 645 -375
		f 4 -646 -392 -27 -376
		f 4 -381 -380 -377 374
		f 4 -383 -382 -378 379
		f 4 -385 -384 468 381
		f 4 -387 -386 -466 383
		f 4 -702 -698 -389 -699
		f 4 388 -391 -390 459
		f 4 -723 724 725 -706
		f 4 -725 -728 729 730
		f 4 -730 -733 734 735
		f 4 -440 -439 437 384
		f 4 -431 -430 410 -691
		f 4 -411 -410 -393 387
		f 4 -475 405 -474 392
		f 4 -406 404 -395 -394
		f 4 -697 -415 -478 393
		f 3 -396 -458 -701
		f 4 -647 -459 390 457
		f 4 458 -412 -47 391
		f 4 -417 -416 395 414
		f 4 -420 396 472 421
		f 4 -473 394 471 422
		f 4 -472 -398 470 423
		f 4 -471 -399 469 424
		f 4 399 -401 -454 -93
		f 4 398 -403 -402 400
		f 4 397 -405 -404 402
		f 4 -476 403 474 -407
		f 4 -477 401 475 408
		f 4 -103 453 476 407
		f 4 -457 -67 -408 427
		f 4 -429 -428 -409 425
		f 4 -427 -426 406 409
		f 4 -414 -413 -49 411
		f 4 480 -308 412 -482
		f 4 415 -418 413 646
		f 4 460 444 -106 -421
		f 4 -461 -422 464 446
		f 4 -465 -423 463 448
		f 4 -464 -424 462 450
		f 4 -463 -425 461 452
		f 4 -436 -74 456 433
		f 4 -435 -434 428 432
		f 4 -433 426 429 -432
		f 4 -470 -400 -95 454
		f 4 -462 -455 -96 455
		f 4 -468 -368 466 376
		f 4 -480 419 420 -127
		f 4 -495 -494 -484 -483
		f 4 -487 -486 -485 482
		f 4 -490 -489 -488 485
		f 4 -493 -492 -491 488
		f 4 -501 493 -497 -496
		f 4 -500 -499 -498 495
		f 4 -543 510 541 -502
		f 4 506 498 438 502
		f 4 -540 537 -503 440
		f 4 501 -537 -536 -504
		f 4 -505 -539 -538 536
		f 4 538 -506 497 -507
		f 4 -542 509 540 504
		f 4 -541 508 500 505
		f 4 535 539 441 -508
		f 4 -509 -513 -512 483
		f 4 -510 -515 -514 512
		f 4 -511 -517 -516 514
		f 4 -519 -518 486 511
		f 4 -521 -520 518 513
		f 4 -523 -522 520 515
		f 4 -525 -524 489 517
		f 4 -527 -526 524 519
		f 4 -529 -528 526 521
		f 4 -535 -534 532 527
		f 4 -533 -532 530 525
		f 4 -531 -530 492 523
		f 4 -191 -544 507 442
		f 4 -193 -545 503 543
		f 4 -195 -546 542 544
		f 4 -197 -547 516 545
		f 4 -548 522 546 -198
		f 4 -549 528 547 -200
		f 4 -550 534 548 -202
		f 4 -552 -551 436 499
		f 4 -555 -554 431 -553
		f 4 -560 -559 553 -556
		f 4 -568 564 559 -557
		f 4 -570 -569 567 491
		f 4 -593 -592 590 -558
		f 4 -562 -561 434 558
		f 4 -563 -216 435 560
		f 4 -591 -590 -589 -564
		f 4 588 -588 -243 580
		f 4 -582 -581 -235 562
		f 4 -583 563 581 561
		f 4 -584 557 582 -565
		f 4 609 -620 -567 -566
		f 4 -572 -571 569 529
		f 4 -574 -573 571 531
		f 4 -576 -575 573 533
		f 4 -585 576 583 568
		f 4 -595 -594 592 -577
		f 4 584 570 -586 -703
		f 4 585 572 -587 -578
		f 4 586 574 -580 -579
		f 4 -599 596 -598 565
		f 4 -602 -258 587 599
		f 4 -601 -600 589 -605
		f 4 -606 -604 -603 604
		f 4 -629 -628 626 603
		f 4 -608 -607 605 591
		f 4 -631 -630 628 606
		f 4 616 -618 607 593
		f 4 634 -637 -617 595
		f 4 -616 614 -609 -610
		f 4 -619 578 -611 613
		f 4 -613 -612 -615 -614
		f 4 577 618 615 597
		f 4 -633 -632 630 617
		f 4 -639 -638 632 636
		f 4 -625 -624 622 600
		f 4 -623 -622 -279 601
		f 4 -627 -626 624 602
		f 4 -636 -635 598 -634
		f 4 -641 -640 638 635
		f 4 640 633 566 -621
		f 4 -642 575 549 -300
		f 4 -643 579 641 -302
		f 4 -644 610 642 -304
		f 4 -645 612 643 -306
		f 4 647 552 430 550
		f 4 -650 -649 484 650
		f 4 -652 -651 487 652
		f 4 -654 -653 490 654
		f 4 648 -657 -656 494
		f 4 655 -659 -658 496
		f 4 657 -661 -660 551
		f 4 662 -664 -662 554
		f 4 661 -666 -665 555
		f 4 664 -667 -655 556
		f 4 659 667 -663 -648
		f 4 -669 649 669 -671
		f 4 -670 651 671 -673
		f 4 -672 653 673 -675
		f 4 668 -677 -676 656
		f 4 675 -679 -678 658
		f 4 677 -681 -680 660
		f 4 682 -684 -682 663
		f 4 681 -686 -685 665
		f 4 684 -687 -674 666
		f 4 679 687 -683 -668
		f 4 -693 674 686 -692
		f 4 683 -688 -696 693
		f 4 685 -694 -695 691
		f 4 -438 -437 690 386
		f 4 670 672 692 -690
		f 4 -689 676 689 694
		f 4 680 678 688 695
		f 4 -479 418 696 -397
		f 4 -419 481 417 416
		f 4 -460 367 699 698
		f 4 697 473 477 700
		f 4 385 -388 701 -379
		f 4 -597 -596 594 702
		f 4 478 479 -367 -481
		f 4 -10 706 707 -705
		f 4 81 703 -711 -709
		f 4 -15 711 712 -707
		f 4 80 708 -716 -714
		f 4 -17 716 717 -712
		f 4 -79 718 719 -717
		f 4 79 713 -721 -719
		f 4 -443 721 722 -704
		f 4 375 704 -726 -724
		f 4 -442 726 727 -722
		f 4 380 723 -731 -729
		f 4 -441 731 732 -727
		f 4 439 733 -735 -732
		f 4 382 728 -736 -734;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vs" 6;
	setAttr ".bw" 6;
createNode transform -n "mocap_arm_PLY" -p "mocap_geometry_GRP";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023BE";
	setAttr ".ove" yes;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode mesh -n "mocap_arm_PLYShape" -p "mocap_arm_PLY";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023BF";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ugsdt" no;
	setAttr ".vs" 6;
	setAttr ".vcs" 2;
createNode mesh -n "polySurfaceShape3" -p "mocap_arm_PLY";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023C0";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ugsdt" no;
	setAttr -s 252 ".vt";
	setAttr ".vt[0:165]"  7.96785259 13.38003826 -0.24628213 8.029249191 13.46340942 0.01534602
		 7.93514347 13.21340656 -0.20230192 7.98555946 13.23991776 0.019068152 7.83003712 13.14336395 -0.36249599
		 7.86900949 13.3232708 -0.42091903 7.98765898 13.43993568 0.28535941 7.98054218 13.20728588 0.25385445
		 7.90221691 13.4019289 0.48454803 7.88726377 13.19023609 0.44030148 7.34494829 13.20183563 0.67418027
		 7.28183842 13.10055447 0.66787446 7.3029151 13.0091991425 0.57713246 7.50238228 13.13481998 0.48058742
		 7.54633331 12.93516541 0.82254517 7.68174028 13.050235748 0.74486828 7.76480484 12.81649208 0.70834297
		 7.78955555 12.84663677 0.70882207 7.74360847 12.8266468 0.87307107 7.81457472 12.86926842 0.81505692
		 7.75498819 12.79793644 0.81797504 7.46008825 13.074612617 0.43544996 7.63160849 12.89520264 0.62066764
		 7.67004871 12.95932674 0.62542832 7.78991842 12.88781357 0.87609076 7.61555099 13.029778481 0.81844091
		 7.46578217 13.25712395 0.56840885 7.58442307 13.15672779 0.24606393 7.40709209 13.4784956 0.44307595
		 7.54613686 13.1913271 0.42543197 7.51344013 13.14380169 0.35849565 7.53735399 12.85693169 0.75254452
		 6.97576284 13.57057095 -0.32833683 6.88060904 13.26929092 0.2957463 6.89548874 13.39486217 0.35752884
		 6.98148251 13.52078819 0.33527622 7.17072582 13.62451553 0.19461237 7.18689585 13.64433956 -0.055596709
		 7.10036993 13.55631542 -0.29939994 7.07496357 13.36374474 0.48398373 7.26794481 13.52264977 -0.32651836
		 7.3727994 13.61022663 0.19135404 7.15435886 13.46290302 0.4372932 7.22501183 13.54522514 0.3586995
		 7.25197411 13.41638184 -0.4104884 7.40849972 13.60936928 -0.0034618974 6.91037273 13.40092564 -0.37075591
		 7.59715366 13.16666889 0.0084944367 7.04693079 13.11669731 0.3630957 7.60875177 13.17801094 -0.15798238
		 7.42369986 13.13606739 -0.14689049 7.24859333 13.16931438 -0.22844452 7.43129396 13.18877697 -0.30137223
		 7.024087906 13.22044086 0.4560971 6.99350452 13.16006374 0.061098024 6.92111397 13.66976357 -0.15580299
		 6.87035751 13.65041733 0.1730141 6.82121897 13.51740456 0.28065321 6.76885271 13.30556107 0.21340424
		 6.92097521 13.19664478 0.18357331 7.015370846 13.35770702 -0.36129305 6.84780264 13.30103111 -0.24008659
		 6.81492949 13.2395525 0.027688757 7.39631987 13.11656666 -0.031578869 7.16917229 13.12958717 -0.081516534
		 7.3820715 13.11401081 0.10176155 7.27191782 13.084796906 0.13973552 6.78186369 13.3940897 0.27256334
		 6.91289139 13.20756149 -0.0164029 6.93870878 13.24821186 -0.19766477 6.61496449 13.52121162 0.27503529
		 6.65593338 13.68091297 -0.19300094 6.62148571 13.28236103 0.20052367 6.66645813 13.54138279 -0.3133086
		 6.66896009 13.42226315 -0.34190392 6.66174555 13.29335308 -0.25945789 6.62486506 13.66101742 0.1619101
		 6.63939619 13.21844959 -0.0041178465 6.61525822 13.38040257 0.27167946 4.23062229 13.66586304 -0.63950825
		 4.23062229 13.38600636 -0.64788574 4.23062229 13.14550114 -0.45928121 4.23062277 13.60603714 0.22652653
		 4.23062229 13.87172127 -0.4650358 4.23062277 13.24217796 0.11768717 4.23062229 13.11375046 -0.14706323
		 4.23062277 13.41950321 0.22977072 4.23062229 13.82478142 0.10276044 4.50077915 13.67054462 -0.62483084
		 4.50077868 13.40173721 -0.62435585 4.50077868 13.18361855 -0.43838394 4.50077868 13.60402775 0.22280329
		 4.50077915 13.87452602 -0.45129001 4.50077915 13.24244595 0.12015826 4.50077868 13.1368885 -0.14416802
		 4.50077868 13.41552925 0.23753256 4.50077868 13.81995583 0.10070739 4.7384758 13.68005562 -0.61829698
		 4.7384758 13.4144125 -0.61120278 4.7384758 13.20383263 -0.43071318 4.7384758 13.60718441 0.24569616
		 4.7384758 13.88354683 -0.44408154 4.7384758 13.22314072 0.13541937 4.7384758 13.13382912 -0.14016962
		 4.7384758 13.40673542 0.26329681 4.7384758 13.8269701 0.11431619 2.0022838116 13.58371067 0.33750749
		 1.99739563 13.88857651 -0.5578928 1.99979281 13.12759304 0.18579096 1.9976629 13.028447151 -0.11684632
		 2.0016942024 13.35496616 0.30872148 2.00094652176 13.86582851 0.15877527 1.99739563 13.64208603 -0.6787886
		 1.99739552 13.36442566 -0.65510774 1.99739552 13.12169933 -0.50695139 8.72973251 12.96432114 -0.13275763
		 8.5286808 12.969594 -0.3013491 8.77156162 12.93949032 0.32308638 8.80587387 12.95946121 0.090863973
		 8.88784122 13.10924721 0.09049204 8.81955338 13.10386372 0.35816878 8.66846371 13.11176586 0.55161178
		 8.6166048 12.96455669 0.50413519 8.59849548 13.090420723 -0.35707262 8.79108143 13.076830864 -0.1742312
		 7.17151451 13.097970009 0.23487319 -7.96785259 13.38003826 -0.24628213 -8.029249191 13.46340942 0.01534602
		 -7.93514347 13.21340656 -0.20230192 -7.98555946 13.23991776 0.019068152 -7.83003712 13.14336395 -0.36249599
		 -7.86900949 13.3232708 -0.42091903 -7.98765898 13.43993568 0.28535941 -7.98054218 13.20728588 0.25385445
		 -7.90221691 13.4019289 0.48454803 -7.88726377 13.19023609 0.44030148 -7.34494829 13.20183563 0.67418027
		 -7.28183842 13.10055447 0.66787446 -7.3029151 13.0091991425 0.57713246 -7.50238228 13.13481998 0.48058742
		 -7.54633331 12.93516541 0.82254517 -7.68174028 13.050235748 0.74486828 -7.76480484 12.81649208 0.70834297
		 -7.78955555 12.84663677 0.70882207 -7.74360847 12.8266468 0.87307107 -7.81457472 12.86926842 0.81505692
		 -7.75498819 12.79793644 0.81797504 -7.46008921 13.074612617 0.43544996 -7.63160849 12.89520264 0.62066764
		 -7.67004871 12.95932674 0.62542832 -7.78991842 12.88781357 0.87609076 -7.61555099 13.029778481 0.81844091
		 -7.46578217 13.25712395 0.56840885 -7.58442307 13.15672779 0.24606393 -7.40709209 13.4784956 0.44307595
		 -7.54613686 13.1913271 0.42543197 -7.51344013 13.14380169 0.35849565 -7.53735399 12.85693169 0.75254452
		 -6.97576284 13.57057095 -0.32833683 -6.88060904 13.26929092 0.2957463 -6.89548779 13.39486217 0.35752884
		 -6.98148251 13.52078819 0.33527622 -7.17072582 13.62451553 0.19461237 -7.18689585 13.64433956 -0.055596709
		 -7.10036993 13.55631542 -0.29939994 -7.07496357 13.36374474 0.48398373;
	setAttr ".vt[166:251]" -7.26794481 13.52264977 -0.32651836 -7.3727994 13.61022663 0.19135404
		 -7.15435886 13.46290302 0.4372932 -7.22501183 13.54522514 0.3586995 -7.25197411 13.41638184 -0.4104884
		 -7.40849972 13.60936928 -0.0034618974 -6.91037273 13.40092564 -0.37075591 -7.59715366 13.16666889 0.0084944367
		 -7.04693079 13.11669731 0.3630957 -7.60875177 13.17801094 -0.15798238 -7.42369986 13.13606739 -0.14689049
		 -7.24859333 13.16931438 -0.22844452 -7.43129396 13.18877697 -0.30137223 -7.024087906 13.22044086 0.4560971
		 -6.99350452 13.16006374 0.061098024 -6.92111397 13.66976357 -0.15580299 -6.87035751 13.65041733 0.1730141
		 -6.82121897 13.51740456 0.28065321 -6.76885271 13.30556107 0.21340424 -6.92097521 13.19664478 0.18357331
		 -7.015370846 13.35770702 -0.36129305 -6.84780264 13.30103111 -0.24008659 -6.81492949 13.2395525 0.027688757
		 -7.39631987 13.11656666 -0.031578869 -7.16917229 13.12958717 -0.081516534 -7.3820715 13.11401081 0.10176155
		 -7.27191782 13.084796906 0.13973552 -6.78186369 13.3940897 0.27256334 -6.91289139 13.20756149 -0.0164029
		 -6.93870878 13.24821186 -0.19766477 -6.61496449 13.52121162 0.27503529 -6.65593338 13.68091297 -0.19300094
		 -6.62148571 13.28236103 0.20052367 -6.66645813 13.54138279 -0.3133086 -6.66896009 13.42226315 -0.34190392
		 -6.66174555 13.29335308 -0.25945789 -6.62486506 13.66101742 0.1619101 -6.63939619 13.21844959 -0.0041178465
		 -6.61525822 13.38040257 0.27167946 -4.23062229 13.66586304 -0.63950825 -4.23062229 13.38600636 -0.64788574
		 -4.23062229 13.14550114 -0.45928121 -4.23062277 13.60603714 0.22652653 -4.23062229 13.87172127 -0.4650358
		 -4.23062277 13.24217796 0.11768717 -4.23062229 13.11375046 -0.14706323 -4.23062277 13.41950321 0.22977072
		 -4.23062229 13.82478142 0.10276044 -4.50077915 13.67054462 -0.62483084 -4.50077868 13.40173721 -0.62435585
		 -4.50077868 13.18361855 -0.43838394 -4.50077868 13.60402775 0.22280329 -4.50077915 13.87452602 -0.45129001
		 -4.50077915 13.24244595 0.12015826 -4.50077868 13.1368885 -0.14416802 -4.50077868 13.41552925 0.23753256
		 -4.50077868 13.81995583 0.10070739 -4.7384758 13.68005562 -0.61829698 -4.7384758 13.4144125 -0.61120278
		 -4.7384758 13.20383263 -0.43071318 -4.7384758 13.60718441 0.24569616 -4.7384758 13.88354683 -0.44408154
		 -4.7384758 13.22314072 0.13541937 -4.7384758 13.13382912 -0.14016962 -4.7384758 13.40673542 0.26329681
		 -4.7384758 13.8269701 0.11431619 -2.0022838116 13.58371067 0.33750749 -1.99739563 13.88857651 -0.5578928
		 -1.99979281 13.12759304 0.18579096 -1.9976629 13.028447151 -0.11684632 -2.0016942024 13.35496616 0.30872148
		 -2.00094652176 13.86582851 0.15877527 -1.99739563 13.64208603 -0.6787886 -1.99739552 13.36442566 -0.65510774
		 -1.99739552 13.12169933 -0.50695139 -8.72973251 12.96432114 -0.13275763 -8.5286808 12.969594 -0.3013491
		 -8.77156162 12.93949032 0.32308638 -8.80587387 12.95946121 0.090863973 -8.88784122 13.10924721 0.09049204
		 -8.81955338 13.10386372 0.35816878 -8.66846371 13.11176586 0.55161178 -8.6166048 12.96455669 0.50413519
		 -8.59849548 13.090420723 -0.35707262 -8.79108143 13.076830864 -0.1742312 -7.17151451 13.097970009 0.23487319;
	setAttr -s 492 ".ed";
	setAttr ".ed[0:165]"  2 4 1 7 3 1 1 6 1 9 7 1 6 8 1 10 26 1 17 16 1 20 18 1
		 18 14 1 16 20 1 17 23 1 23 22 1 22 21 1 22 31 1 19 20 1 24 19 1 25 15 1 15 26 1 24 18 1
		 17 19 1 28 29 1 4 5 1 8 9 1 23 13 1 13 26 1 25 10 1 10 11 1 12 31 1 11 12 1 21 13 1
		 3 2 1 66 30 1 30 21 1 41 6 1 1 45 1 2 49 1 9 29 1 8 28 1 0 5 1 12 21 1 31 14 1 14 11 1
		 15 23 1 29 30 1 30 27 1 29 13 1 31 20 1 22 16 1 19 15 1 25 24 1 25 14 1 58 33 1 33 34 1
		 34 67 1 67 58 1 34 35 1 35 57 1 57 67 1 36 56 1 56 57 1 35 36 1 36 37 1 38 40 1 32 38 1
		 4 52 1 52 44 1 5 44 1 44 40 1 26 42 1 42 39 1 39 10 1 43 28 1 40 45 1 43 42 1 37 45 1
		 60 44 1 42 35 1 34 39 1 41 45 1 43 36 1 55 37 1 63 47 1 50 49 1 49 47 1 3 47 1 11 53 1
		 53 48 1 48 12 1 66 65 1 65 27 1 66 64 1 51 50 1 63 64 1 64 51 1 51 52 1 52 49 1 65 63 1
		 60 51 1 64 69 1 39 53 1 33 53 1 60 38 1 48 59 1 59 54 1 33 59 1 32 46 1 62 58 1 60 46 1
		 62 59 1 27 7 1 62 68 1 68 54 1 41 36 1 55 56 1 68 69 1 61 62 1 48 125 1 69 60 1 61 69 1
		 32 73 1 46 74 1 61 75 1 32 55 1 38 37 1 0 1 1 50 63 1 46 61 1 70 57 1 71 55 1 72 58 1
		 73 97 1 75 99 1 76 56 1 77 62 1 78 67 1 77 72 1 78 70 1 70 76 1 71 73 1 74 73 1 75 74 1
		 72 78 1 76 71 1 77 75 1 106 82 1 107 83 1 108 84 1 79 112 1 80 113 1 81 114 1 82 91 1
		 83 92 1 84 93 1 85 94 1 86 95 1 87 96 1 83 87 1 84 85 1 82 86 1 82 87 1 83 79 1 84 86 1
		 80 81 1 79 80 1 81 85 1 88 79 1;
	setAttr ".ed[166:331]" 89 80 1 90 81 1 91 100 1 92 101 1 93 102 1 94 103 1
		 95 104 1 96 105 1 92 96 1 93 94 1 91 95 1 91 96 1 92 88 1 93 95 1 89 90 1 88 89 1
		 90 94 1 97 88 1 98 89 1 99 90 1 103 77 1 104 78 1 101 105 1 102 103 1 100 104 1 100 105 1
		 101 97 1 102 104 1 98 99 1 97 98 1 99 103 1 101 71 1 74 98 1 100 70 1 102 72 1 105 76 1
		 109 85 1 110 86 1 111 87 1 106 111 0 107 112 0 108 110 0 113 114 0 112 113 0 114 109 0
		 107 111 0 108 109 0 106 110 0 2 115 1 4 116 1 115 116 1 116 123 1 7 117 1 3 118 1
		 117 118 1 1 119 1 6 120 1 119 120 1 8 121 1 121 122 1 9 122 1 122 117 1 120 121 1
		 5 123 1 118 115 1 0 124 1 124 123 1 124 119 1 0 40 1 118 119 1 117 120 1 115 124 1
		 26 28 1 125 66 1 21 125 1 125 54 1 27 29 1 28 41 1 54 64 1 47 27 1 128 130 1 133 129 1
		 127 132 1 135 133 1 132 134 1 136 152 1 143 142 1 146 144 1 144 140 1 142 146 1 143 149 1
		 149 148 1 148 147 1 148 157 1 145 146 1 150 145 1 151 141 1 141 152 1 150 144 1 143 145 1
		 154 155 1 130 131 1 134 135 1 149 139 1 139 152 1 151 136 1 136 137 1 138 157 1 137 138 1
		 147 139 1 129 128 1 192 156 1 156 147 1 167 132 1 127 171 1 128 175 1 135 155 1 134 154 1
		 126 131 1 138 147 1 157 140 1 140 137 1 141 149 1 155 156 1 156 153 1 155 139 1 157 146 1
		 148 142 1 145 141 1 151 150 1 151 140 1 184 159 1 159 160 1 160 193 1 193 184 1 160 161 1
		 161 183 1 183 193 1 162 182 1 182 183 1 161 162 1 162 163 1 164 166 1 158 164 1 130 178 1
		 178 170 1 131 170 1 170 166 1 152 168 1 168 165 1 165 136 1 169 154 1 166 171 1 169 168 1
		 163 171 1 186 170 1 168 161 1 160 165 1 167 171 1 169 162 1 181 163 1 189 173 1 176 175 1
		 175 173 1 129 173 1 137 179 1;
	setAttr ".ed[332:491]" 179 174 1 174 138 1 192 191 1 191 153 1 192 190 1 177 176 1
		 189 190 1 190 177 1 177 178 1 178 175 1 191 189 1 186 177 1 190 195 1 165 179 1 159 179 1
		 186 164 1 174 185 1 185 180 1 159 185 1 158 172 1 188 184 1 186 172 1 188 185 1 153 133 1
		 188 194 1 194 180 1 167 162 1 181 182 1 194 195 1 187 188 1 174 251 1 195 186 1 187 195 1
		 158 199 1 172 200 1 187 201 1 158 181 1 164 163 1 126 127 1 176 189 1 172 187 1 196 183 1
		 197 181 1 198 184 1 199 223 1 201 225 1 202 182 1 203 188 1 204 193 1 203 198 1 204 196 1
		 196 202 1 197 199 1 200 199 1 201 200 1 198 204 1 202 197 1 203 201 1 232 208 1 233 209 1
		 234 210 1 205 238 1 206 239 1 207 240 1 208 217 1 209 218 1 210 219 1 211 220 1 212 221 1
		 213 222 1 209 213 1 210 211 1 208 212 1 208 213 1 209 205 1 210 212 1 206 207 1 205 206 1
		 207 211 1 214 205 1 215 206 1 216 207 1 217 226 1 218 227 1 219 228 1 220 229 1 221 230 1
		 222 231 1 218 222 1 219 220 1 217 221 1 217 222 1 218 214 1 219 221 1 215 216 1 214 215 1
		 216 220 1 223 214 1 224 215 1 225 216 1 229 203 1 230 204 1 227 231 1 228 229 1 226 230 1
		 226 231 1 227 223 1 228 230 1 224 225 1 223 224 1 225 229 1 227 197 1 200 224 1 226 196 1
		 228 198 1 231 202 1 235 211 1 236 212 1 237 213 1 232 237 0 233 238 0 234 236 0 239 240 0
		 238 239 0 240 235 0 233 237 0 234 235 0 232 236 0 128 241 1 130 242 1 241 242 1 242 249 1
		 133 243 1 129 244 1 243 244 1 127 245 1 132 246 1 245 246 1 134 247 1 247 248 1 135 248 1
		 248 243 1 246 247 1 131 249 1 244 241 1 126 250 1 250 249 1 250 245 1 126 166 1 244 245 1
		 243 246 1 241 250 1 152 154 1 251 192 1 147 251 1 251 180 1 153 155 1 154 167 1 180 190 1
		 173 153 1;
	setAttr -s 242 -ch 966 ".fc[0:241]" -type "polyFaces" 
		f 4 5 68 69 70
		f 4 6 -48 -12 -11
		f 4 7 8 -41 46
		f 4 9 -47 -14 47
		f 4 11 12 29 -24
		f 4 -13 13 -28 39
		f 4 14 -10 -7 19
		f 4 -18 42 23 24
		f 4 15 48 -17 49
		f 4 16 17 -6 -26
		f 4 -8 -15 -16 18
		f 4 -20 10 -43 -49
		f 4 37 20 -37 -23
		f 4 71 243 112 -80
		f 4 64 65 -67 -22
		f 4 -1 35 -96 -65
		f 4 25 26 -42 -51
		f 4 28 27 40 41
		f 4 -29 85 86 87
		f 4 -27 -71 99 -86
		f 4 33 -3 34 -79
		f 4 84 -84 -36 -31
		f 3 242 43 44
		f 4 -35 -125 234 72
		f 4 31 32 240 239
		f 4 -45 -32 88 89
		f 4 45 -30 -33 -44
		f 4 238 -72 73 -69
		f 4 -9 -19 -50 50
		f 4 51 52 53 54
		f 4 55 56 57 -54
		f 4 58 59 -57 60
		f 4 135 -201 189 186
		f 4 136 -200 190 187
		f 4 123 74 -73 -63
		f 4 75 -66 -95 -98
		f 4 -70 76 -56 77
		f 4 78 -75 -62 -113
		f 4 -61 -77 -74 79
		f 4 -64 122 80 -124
		f 4 -59 61 -81 113
		f 4 96 81 245 -90
		f 4 82 83 -82 -126
		f 4 -89 90 -93 -97
		f 4 91 125 92 93
		f 4 -83 -92 94 95
		f 4 97 -94 98 117
		f 4 100 -100 -78 -53
		f 4 62 -68 -76 101
		f 4 -103 -87 -101 104
		f 4 105 120 139 -120
		f 4 126 121 140 -121
		f 4 -102 107 -106 63
		f 4 -107 108 -105 -52
		f 4 -109 110 111 -104
		f 4 115 -134 143 -122
		f 4 -91 -240 241 244
		f 4 -111 -116 118 -115
		f 4 -108 -118 -119 -127
		f 4 132 -114 -129 -143
		f 4 -136 133 106 -130
		f 4 -137 134 -58 -128
		f 4 -138 127 -60 -133
		f 4 -139 128 -123 119
		f 4 -142 129 -55 -135
		f 4 -157 -146 211 204
		f 4 -158 -147 212 202
		f 4 -159 -145 213 203
		f 4 -160 150 177 -156
		f 4 -161 151 178 165
		f 4 -162 152 179 -155
		f 4 -163 -167 180 167
		f 4 -164 -166 181 166
		f 4 -165 -168 182 -154
		f 4 156 155 -175 -152
		f 4 -176 -153 157 153
		f 4 -177 -151 158 154
		f 4 -178 168 191 -174
		f 4 -179 169 192 183
		f 4 -180 170 193 -173
		f 4 -181 -185 194 185
		f 4 -182 -184 195 184
		f 4 -183 -186 196 -172
		f 4 174 173 -189 -170
		f 4 -190 -171 175 171
		f 4 -191 -169 176 172
		f 4 -192 199 137 -202
		f 4 -193 197 138 130
		f 4 -188 -194 200 141
		f 4 -195 -199 -141 131
		f 4 -196 -131 -140 198
		f 4 -187 -197 -132 -144
		f 4 201 142 -198 188
		f 4 -205 -206 144 159
		f 4 -207 145 160 147
		f 4 -204 -208 146 161
		f 4 -209 -149 162 149
		f 4 -210 -148 163 148
		f 4 -203 -211 -150 164
		f 4 0 215 -217 -215
		f 4 -218 -216 21 229
		f 4 1 219 -221 -219
		f 4 2 222 -224 -222
		f 4 -226 -225 22 226
		f 4 3 218 -228 -227
		f 4 4 224 -229 -223
		f 4 30 214 -231 -220
		f 4 -39 231 232 -230
		f 4 124 221 -234 -232
		f 4 -235 38 66 67
		f 4 220 235 223 -237
		f 4 233 -236 230 237
		f 4 217 -233 -238 216
		f 4 227 236 228 225
		f 4 -25 -46 -21 -239
		f 4 -241 -40 -88 116
		f 4 -242 -117 102 103
		f 4 109 -4 36 -243
		f 4 -38 -5 -34 -244
		f 4 -112 114 -99 -245
		f 4 -246 -85 -2 -110
		f 4 -317 -316 -315 -252
		f 4 256 257 293 -253
		f 4 -293 286 -255 -254
		f 4 -294 259 292 -256
		f 4 269 -276 -259 -258
		f 4 -286 273 -260 258
		f 4 -266 252 255 -261
		f 4 -271 -270 -289 263
		f 4 -296 262 -295 -262
		f 4 271 251 -264 -263
		f 4 -265 261 260 253
		f 4 294 288 -257 265
		f 4 268 282 -267 -284
		f 4 325 -359 -490 -318
		f 4 267 312 -312 -311
		f 4 310 341 -282 246
		f 4 296 287 -273 -272
		f 4 -288 -287 -274 -275
		f 4 -334 -333 -332 274
		f 4 331 -346 316 272
		f 4 324 -281 248 -280
		f 4 276 281 329 -331
		f 3 -291 -290 -489
		f 4 -319 -481 370 280
		f 4 -486 -487 -279 -278
		f 4 -336 -335 277 290
		f 4 289 278 275 -292
		f 4 314 -320 317 -485
		f 4 -297 295 264 254
		f 4 -301 -300 -299 -298
		f 4 299 -304 -303 -302
		f 4 -307 302 -306 -305
		f 4 -433 -436 446 -382
		f 4 -434 -437 445 -383
		f 4 308 318 -321 -370
		f 4 343 340 311 -322
		f 4 -324 301 -323 315
		f 4 358 307 320 -325
		f 4 -326 319 322 306
		f 4 369 -327 -369 309
		f 4 -360 326 -308 304
		f 4 335 -492 -328 -343
		f 4 371 327 -330 -329
		f 4 342 338 -337 334
		f 4 -340 -339 -372 -338
		f 4 -342 -341 337 328
		f 4 -364 -345 339 -344
		f 4 298 323 345 -347
		f 4 -348 321 313 -309
		f 4 -351 346 332 348
		f 4 365 -386 -367 -352
		f 4 366 -387 -368 -373
		f 4 -310 351 -354 347
		f 4 297 350 -355 352
		f 4 349 -358 -357 354
		f 4 367 -390 379 -362
		f 4 -491 -488 485 336
		f 4 360 -365 361 356
		f 4 372 364 363 353
		f 4 388 374 359 -379
		f 4 375 -353 -380 381
		f 4 373 303 -381 382
		f 4 378 305 -374 383
		f 4 -366 368 -375 384
		f 4 380 300 -376 387
		f 4 -451 -458 391 402
		f 4 -449 -459 392 403
		f 4 -450 -460 390 404
		f 4 401 -424 -397 405
		f 4 -412 -425 -398 406
		f 4 400 -426 -399 407
		f 4 -414 -427 412 408
		f 4 -413 -428 411 409
		f 4 399 -429 413 410
		f 4 397 420 -402 -403
		f 4 -400 -404 398 421
		f 4 -401 -405 396 422
		f 4 419 -438 -415 423
		f 4 -430 -439 -416 424
		f 4 418 -440 -417 425
		f 4 -432 -441 430 426
		f 4 -431 -442 429 427
		f 4 417 -443 431 428
		f 4 415 434 -420 -421
		f 4 -418 -422 416 435
		f 4 -419 -423 414 436
		f 4 447 -384 -446 437
		f 4 -377 -385 -444 438
		f 4 -388 -447 439 433
		f 4 -378 386 444 440
		f 4 -445 385 376 441
		f 4 389 377 442 432
		f 4 -435 443 -389 -448
		f 4 -406 -391 451 450
		f 4 -394 -407 -392 452
		f 4 -408 -393 453 449
		f 4 -396 -409 394 454
		f 4 -395 -410 393 455
		f 4 -411 395 456 448
		f 4 460 462 -462 -247
		f 4 -476 -268 461 463
		f 4 464 466 -466 -248
		f 4 467 469 -469 -249
		f 4 -473 -269 470 471
		f 4 472 473 -465 -250
		f 4 468 474 -471 -251
		f 4 465 476 -461 -277
		f 4 475 -479 -478 284
		f 4 477 479 -468 -371
		f 4 -314 -313 -285 480
		f 4 482 -470 -482 -467
		f 4 -484 -477 481 -480
		f 4 -463 483 478 -464
		f 4 -472 -475 -483 -474
		f 4 484 266 291 270
		f 4 -363 333 285 486
		f 4 -350 -349 362 487
		f 4 488 -283 249 -356
		f 4 489 279 250 283
		f 4 490 344 -361 357
		f 4 355 247 330 491;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vs" 6;
createNode mesh -n "mocap_arm_PLYShapeOrig" -p "mocap_arm_PLY";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023C1";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ugsdt" no;
	setAttr -s 252 ".vt";
	setAttr ".vt[0:165]"  7.96785259 13.38003826 -0.24628213 8.029249191 13.46340942 0.01534602
		 7.93514347 13.21340656 -0.20230192 7.98555946 13.23991776 0.019068152 7.83003712 13.14336395 -0.36249599
		 7.86900949 13.3232708 -0.42091903 7.98765898 13.43993568 0.28535941 7.98054218 13.20728588 0.25385445
		 7.90221691 13.4019289 0.48454803 7.88726377 13.19023609 0.44030148 7.34494829 13.20183563 0.67418027
		 7.28183842 13.10055447 0.66787446 7.3029151 13.0091991425 0.57713246 7.50238228 13.13481998 0.48058742
		 7.54633331 12.93516541 0.82254517 7.68174028 13.050235748 0.74486828 7.76480484 12.81649208 0.70834297
		 7.78955555 12.84663677 0.70882207 7.74360847 12.8266468 0.87307107 7.81457472 12.86926842 0.81505692
		 7.75498819 12.79793644 0.81797504 7.46008825 13.074612617 0.43544996 7.63160849 12.89520264 0.62066764
		 7.67004871 12.95932674 0.62542832 7.78991842 12.88781357 0.87609076 7.61555099 13.029778481 0.81844091
		 7.46578217 13.25712395 0.56840885 7.58442307 13.15672779 0.24606393 7.40709209 13.4784956 0.44307595
		 7.54613686 13.1913271 0.42543197 7.51344013 13.14380169 0.35849565 7.53735399 12.85693169 0.75254452
		 6.97576284 13.57057095 -0.32833683 6.88060904 13.26929092 0.2957463 6.89548874 13.39486217 0.35752884
		 6.98148251 13.52078819 0.33527622 7.17072582 13.62451553 0.19461237 7.18689585 13.64433956 -0.055596709
		 7.10036993 13.55631542 -0.29939994 7.07496357 13.36374474 0.48398373 7.26794481 13.52264977 -0.32651836
		 7.3727994 13.61022663 0.19135404 7.15435886 13.46290302 0.4372932 7.22501183 13.54522514 0.3586995
		 7.25197411 13.41638184 -0.4104884 7.40849972 13.60936928 -0.0034618974 6.91037273 13.40092564 -0.37075591
		 7.59715366 13.16666889 0.0084944367 7.04693079 13.11669731 0.3630957 7.60875177 13.17801094 -0.15798238
		 7.42369986 13.13606739 -0.14689049 7.24859333 13.16931438 -0.22844452 7.43129396 13.18877697 -0.30137223
		 7.024087906 13.22044086 0.4560971 6.99350452 13.16006374 0.061098024 6.92111397 13.66976357 -0.15580299
		 6.87035751 13.65041733 0.1730141 6.82121897 13.51740456 0.28065321 6.76885271 13.30556107 0.21340424
		 6.92097521 13.19664478 0.18357331 7.015370846 13.35770702 -0.36129305 6.84780264 13.30103111 -0.24008659
		 6.81492949 13.2395525 0.027688757 7.39631987 13.11656666 -0.031578869 7.16917229 13.12958717 -0.081516534
		 7.3820715 13.11401081 0.10176155 7.27191782 13.084796906 0.13973552 6.78186369 13.3940897 0.27256334
		 6.91289139 13.20756149 -0.0164029 6.93870878 13.24821186 -0.19766477 6.61496449 13.52121162 0.27503529
		 6.65593338 13.68091297 -0.19300094 6.62148571 13.28236103 0.20052367 6.66645813 13.54138279 -0.3133086
		 6.66896009 13.42226315 -0.34190392 6.66174555 13.29335308 -0.25945789 6.62486506 13.66101742 0.1619101
		 6.63939619 13.21844959 -0.0041178465 6.61525822 13.38040257 0.27167946 4.23062229 13.66586304 -0.63950825
		 4.23062229 13.38600636 -0.64788574 4.23062229 13.14550114 -0.45928121 4.23062277 13.60603714 0.22652653
		 4.23062229 13.87172127 -0.4650358 4.23062277 13.24217796 0.11768717 4.23062229 13.11375046 -0.14706323
		 4.23062277 13.41950321 0.22977072 4.23062229 13.82478142 0.10276044 4.50077915 13.67054462 -0.62483084
		 4.50077868 13.40173721 -0.62435585 4.50077868 13.18361855 -0.43838394 4.50077868 13.60402775 0.22280329
		 4.50077915 13.87452602 -0.45129001 4.50077915 13.24244595 0.12015826 4.50077868 13.1368885 -0.14416802
		 4.50077868 13.41552925 0.23753256 4.50077868 13.81995583 0.10070739 4.7384758 13.68005562 -0.61829698
		 4.7384758 13.4144125 -0.61120278 4.7384758 13.20383263 -0.43071318 4.7384758 13.60718441 0.24569616
		 4.7384758 13.88354683 -0.44408154 4.7384758 13.22314072 0.13541937 4.7384758 13.13382912 -0.14016962
		 4.7384758 13.40673542 0.26329681 4.7384758 13.8269701 0.11431619 2.0022838116 13.58371067 0.33750749
		 1.99739563 13.88857651 -0.5578928 1.99979281 13.12759304 0.18579096 1.9976629 13.028447151 -0.11684632
		 2.0016942024 13.35496616 0.30872148 2.00094652176 13.86582851 0.15877527 1.99739563 13.64208603 -0.6787886
		 1.99739552 13.36442566 -0.65510774 1.99739552 13.12169933 -0.50695139 8.72973251 12.96432114 -0.13275763
		 8.5286808 12.969594 -0.3013491 8.77156162 12.93949032 0.32308638 8.80587387 12.95946121 0.090863973
		 8.88784122 13.10924721 0.09049204 8.81955338 13.10386372 0.35816878 8.66846371 13.11176586 0.55161178
		 8.6166048 12.96455669 0.50413519 8.59849548 13.090420723 -0.35707262 8.79108143 13.076830864 -0.1742312
		 7.17151451 13.097970009 0.23487319 -7.96785259 13.38003826 -0.24628213 -8.029249191 13.46340942 0.01534602
		 -7.93514347 13.21340656 -0.20230192 -7.98555946 13.23991776 0.019068152 -7.83003712 13.14336395 -0.36249599
		 -7.86900949 13.3232708 -0.42091903 -7.98765898 13.43993568 0.28535941 -7.98054218 13.20728588 0.25385445
		 -7.90221691 13.4019289 0.48454803 -7.88726377 13.19023609 0.44030148 -7.34494829 13.20183563 0.67418027
		 -7.28183842 13.10055447 0.66787446 -7.3029151 13.0091991425 0.57713246 -7.50238228 13.13481998 0.48058742
		 -7.54633331 12.93516541 0.82254517 -7.68174028 13.050235748 0.74486828 -7.76480484 12.81649208 0.70834297
		 -7.78955555 12.84663677 0.70882207 -7.74360847 12.8266468 0.87307107 -7.81457472 12.86926842 0.81505692
		 -7.75498819 12.79793644 0.81797504 -7.46008921 13.074612617 0.43544996 -7.63160849 12.89520264 0.62066764
		 -7.67004871 12.95932674 0.62542832 -7.78991842 12.88781357 0.87609076 -7.61555099 13.029778481 0.81844091
		 -7.46578217 13.25712395 0.56840885 -7.58442307 13.15672779 0.24606393 -7.40709209 13.4784956 0.44307595
		 -7.54613686 13.1913271 0.42543197 -7.51344013 13.14380169 0.35849565 -7.53735399 12.85693169 0.75254452
		 -6.97576284 13.57057095 -0.32833683 -6.88060904 13.26929092 0.2957463 -6.89548779 13.39486217 0.35752884
		 -6.98148251 13.52078819 0.33527622 -7.17072582 13.62451553 0.19461237 -7.18689585 13.64433956 -0.055596709
		 -7.10036993 13.55631542 -0.29939994 -7.07496357 13.36374474 0.48398373;
	setAttr ".vt[166:251]" -7.26794481 13.52264977 -0.32651836 -7.3727994 13.61022663 0.19135404
		 -7.15435886 13.46290302 0.4372932 -7.22501183 13.54522514 0.3586995 -7.25197411 13.41638184 -0.4104884
		 -7.40849972 13.60936928 -0.0034618974 -6.91037273 13.40092564 -0.37075591 -7.59715366 13.16666889 0.0084944367
		 -7.04693079 13.11669731 0.3630957 -7.60875177 13.17801094 -0.15798238 -7.42369986 13.13606739 -0.14689049
		 -7.24859333 13.16931438 -0.22844452 -7.43129396 13.18877697 -0.30137223 -7.024087906 13.22044086 0.4560971
		 -6.99350452 13.16006374 0.061098024 -6.92111397 13.66976357 -0.15580299 -6.87035751 13.65041733 0.1730141
		 -6.82121897 13.51740456 0.28065321 -6.76885271 13.30556107 0.21340424 -6.92097521 13.19664478 0.18357331
		 -7.015370846 13.35770702 -0.36129305 -6.84780264 13.30103111 -0.24008659 -6.81492949 13.2395525 0.027688757
		 -7.39631987 13.11656666 -0.031578869 -7.16917229 13.12958717 -0.081516534 -7.3820715 13.11401081 0.10176155
		 -7.27191782 13.084796906 0.13973552 -6.78186369 13.3940897 0.27256334 -6.91289139 13.20756149 -0.0164029
		 -6.93870878 13.24821186 -0.19766477 -6.61496449 13.52121162 0.27503529 -6.65593338 13.68091297 -0.19300094
		 -6.62148571 13.28236103 0.20052367 -6.66645813 13.54138279 -0.3133086 -6.66896009 13.42226315 -0.34190392
		 -6.66174555 13.29335308 -0.25945789 -6.62486506 13.66101742 0.1619101 -6.63939619 13.21844959 -0.0041178465
		 -6.61525822 13.38040257 0.27167946 -4.23062229 13.66586304 -0.63950825 -4.23062229 13.38600636 -0.64788574
		 -4.23062229 13.14550114 -0.45928121 -4.23062277 13.60603714 0.22652653 -4.23062229 13.87172127 -0.4650358
		 -4.23062277 13.24217796 0.11768717 -4.23062229 13.11375046 -0.14706323 -4.23062277 13.41950321 0.22977072
		 -4.23062229 13.82478142 0.10276044 -4.50077915 13.67054462 -0.62483084 -4.50077868 13.40173721 -0.62435585
		 -4.50077868 13.18361855 -0.43838394 -4.50077868 13.60402775 0.22280329 -4.50077915 13.87452602 -0.45129001
		 -4.50077915 13.24244595 0.12015826 -4.50077868 13.1368885 -0.14416802 -4.50077868 13.41552925 0.23753256
		 -4.50077868 13.81995583 0.10070739 -4.7384758 13.68005562 -0.61829698 -4.7384758 13.4144125 -0.61120278
		 -4.7384758 13.20383263 -0.43071318 -4.7384758 13.60718441 0.24569616 -4.7384758 13.88354683 -0.44408154
		 -4.7384758 13.22314072 0.13541937 -4.7384758 13.13382912 -0.14016962 -4.7384758 13.40673542 0.26329681
		 -4.7384758 13.8269701 0.11431619 -2.0022838116 13.58371067 0.33750749 -1.99739563 13.88857651 -0.5578928
		 -1.99979281 13.12759304 0.18579096 -1.9976629 13.028447151 -0.11684632 -2.0016942024 13.35496616 0.30872148
		 -2.00094652176 13.86582851 0.15877527 -1.99739563 13.64208603 -0.6787886 -1.99739552 13.36442566 -0.65510774
		 -1.99739552 13.12169933 -0.50695139 -8.72973251 12.96432114 -0.13275763 -8.5286808 12.969594 -0.3013491
		 -8.77156162 12.93949032 0.32308638 -8.80587387 12.95946121 0.090863973 -8.88784122 13.10924721 0.09049204
		 -8.81955338 13.10386372 0.35816878 -8.66846371 13.11176586 0.55161178 -8.6166048 12.96455669 0.50413519
		 -8.59849548 13.090420723 -0.35707262 -8.79108143 13.076830864 -0.1742312 -7.17151451 13.097970009 0.23487319;
	setAttr -s 492 ".ed";
	setAttr ".ed[0:165]"  2 4 1 7 3 1 1 6 1 9 7 1 6 8 1 10 26 1 17 16 1 20 18 1
		 18 14 1 16 20 1 17 23 1 23 22 1 22 21 1 22 31 1 19 20 1 24 19 1 25 15 1 15 26 1 24 18 1
		 17 19 1 28 29 1 4 5 1 8 9 1 23 13 1 13 26 1 25 10 1 10 11 1 12 31 1 11 12 1 21 13 1
		 3 2 1 66 30 1 30 21 1 41 6 1 1 45 1 2 49 1 9 29 1 8 28 1 0 5 1 12 21 1 31 14 1 14 11 1
		 15 23 1 29 30 1 30 27 1 29 13 1 31 20 1 22 16 1 19 15 1 25 24 1 25 14 1 58 33 1 33 34 1
		 34 67 1 67 58 1 34 35 1 35 57 1 57 67 1 36 56 1 56 57 1 35 36 1 36 37 1 38 40 1 32 38 1
		 4 52 1 52 44 1 5 44 1 44 40 1 26 42 1 42 39 1 39 10 1 43 28 1 40 45 1 43 42 1 37 45 1
		 60 44 1 42 35 1 34 39 1 41 45 1 43 36 1 55 37 1 63 47 1 50 49 1 49 47 1 3 47 1 11 53 1
		 53 48 1 48 12 1 66 65 1 65 27 1 66 64 1 51 50 1 63 64 1 64 51 1 51 52 1 52 49 1 65 63 1
		 60 51 1 64 69 1 39 53 1 33 53 1 60 38 1 48 59 1 59 54 1 33 59 1 32 46 1 62 58 1 60 46 1
		 62 59 1 27 7 1 62 68 1 68 54 1 41 36 1 55 56 1 68 69 1 61 62 1 48 125 1 69 60 1 61 69 1
		 32 73 1 46 74 1 61 75 1 32 55 1 38 37 1 0 1 1 50 63 1 46 61 1 70 57 1 71 55 1 72 58 1
		 73 97 1 75 99 1 76 56 1 77 62 1 78 67 1 77 72 1 78 70 1 70 76 1 71 73 1 74 73 1 75 74 1
		 72 78 1 76 71 1 77 75 1 106 82 1 107 83 1 108 84 1 79 112 1 80 113 1 81 114 1 82 91 1
		 83 92 1 84 93 1 85 94 1 86 95 1 87 96 1 83 87 1 84 85 1 82 86 1 82 87 1 83 79 1 84 86 1
		 80 81 1 79 80 1 81 85 1 88 79 1;
	setAttr ".ed[166:331]" 89 80 1 90 81 1 91 100 1 92 101 1 93 102 1 94 103 1
		 95 104 1 96 105 1 92 96 1 93 94 1 91 95 1 91 96 1 92 88 1 93 95 1 89 90 1 88 89 1
		 90 94 1 97 88 1 98 89 1 99 90 1 103 77 1 104 78 1 101 105 1 102 103 1 100 104 1 100 105 1
		 101 97 1 102 104 1 98 99 1 97 98 1 99 103 1 101 71 1 74 98 1 100 70 1 102 72 1 105 76 1
		 109 85 1 110 86 1 111 87 1 106 111 0 107 112 0 108 110 0 113 114 0 112 113 0 114 109 0
		 107 111 0 108 109 0 106 110 0 2 115 1 4 116 1 115 116 1 116 123 1 7 117 1 3 118 1
		 117 118 1 1 119 1 6 120 1 119 120 1 8 121 1 121 122 1 9 122 1 122 117 1 120 121 1
		 5 123 1 118 115 1 0 124 1 124 123 1 124 119 1 0 40 1 118 119 1 117 120 1 115 124 1
		 26 28 1 125 66 1 21 125 1 125 54 1 27 29 1 28 41 1 54 64 1 47 27 1 128 130 1 133 129 1
		 127 132 1 135 133 1 132 134 1 136 152 1 143 142 1 146 144 1 144 140 1 142 146 1 143 149 1
		 149 148 1 148 147 1 148 157 1 145 146 1 150 145 1 151 141 1 141 152 1 150 144 1 143 145 1
		 154 155 1 130 131 1 134 135 1 149 139 1 139 152 1 151 136 1 136 137 1 138 157 1 137 138 1
		 147 139 1 129 128 1 192 156 1 156 147 1 167 132 1 127 171 1 128 175 1 135 155 1 134 154 1
		 126 131 1 138 147 1 157 140 1 140 137 1 141 149 1 155 156 1 156 153 1 155 139 1 157 146 1
		 148 142 1 145 141 1 151 150 1 151 140 1 184 159 1 159 160 1 160 193 1 193 184 1 160 161 1
		 161 183 1 183 193 1 162 182 1 182 183 1 161 162 1 162 163 1 164 166 1 158 164 1 130 178 1
		 178 170 1 131 170 1 170 166 1 152 168 1 168 165 1 165 136 1 169 154 1 166 171 1 169 168 1
		 163 171 1 186 170 1 168 161 1 160 165 1 167 171 1 169 162 1 181 163 1 189 173 1 176 175 1
		 175 173 1 129 173 1 137 179 1;
	setAttr ".ed[332:491]" 179 174 1 174 138 1 192 191 1 191 153 1 192 190 1 177 176 1
		 189 190 1 190 177 1 177 178 1 178 175 1 191 189 1 186 177 1 190 195 1 165 179 1 159 179 1
		 186 164 1 174 185 1 185 180 1 159 185 1 158 172 1 188 184 1 186 172 1 188 185 1 153 133 1
		 188 194 1 194 180 1 167 162 1 181 182 1 194 195 1 187 188 1 174 251 1 195 186 1 187 195 1
		 158 199 1 172 200 1 187 201 1 158 181 1 164 163 1 126 127 1 176 189 1 172 187 1 196 183 1
		 197 181 1 198 184 1 199 223 1 201 225 1 202 182 1 203 188 1 204 193 1 203 198 1 204 196 1
		 196 202 1 197 199 1 200 199 1 201 200 1 198 204 1 202 197 1 203 201 1 232 208 1 233 209 1
		 234 210 1 205 238 1 206 239 1 207 240 1 208 217 1 209 218 1 210 219 1 211 220 1 212 221 1
		 213 222 1 209 213 1 210 211 1 208 212 1 208 213 1 209 205 1 210 212 1 206 207 1 205 206 1
		 207 211 1 214 205 1 215 206 1 216 207 1 217 226 1 218 227 1 219 228 1 220 229 1 221 230 1
		 222 231 1 218 222 1 219 220 1 217 221 1 217 222 1 218 214 1 219 221 1 215 216 1 214 215 1
		 216 220 1 223 214 1 224 215 1 225 216 1 229 203 1 230 204 1 227 231 1 228 229 1 226 230 1
		 226 231 1 227 223 1 228 230 1 224 225 1 223 224 1 225 229 1 227 197 1 200 224 1 226 196 1
		 228 198 1 231 202 1 235 211 1 236 212 1 237 213 1 232 237 0 233 238 0 234 236 0 239 240 0
		 238 239 0 240 235 0 233 237 0 234 235 0 232 236 0 128 241 1 130 242 1 241 242 1 242 249 1
		 133 243 1 129 244 1 243 244 1 127 245 1 132 246 1 245 246 1 134 247 1 247 248 1 135 248 1
		 248 243 1 246 247 1 131 249 1 244 241 1 126 250 1 250 249 1 250 245 1 126 166 1 244 245 1
		 243 246 1 241 250 1 152 154 1 251 192 1 147 251 1 251 180 1 153 155 1 154 167 1 180 190 1
		 173 153 1;
	setAttr -s 252 ".n";
	setAttr ".n[0:165]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20;
	setAttr ".n[166:251]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20;
	setAttr -s 242 -ch 966 ".fc[0:241]" -type "polyFaces" 
		f 4 5 68 69 70
		f 4 6 -48 -12 -11
		f 4 7 8 -41 46
		f 4 9 -47 -14 47
		f 4 11 12 29 -24
		f 4 -13 13 -28 39
		f 4 14 -10 -7 19
		f 4 -18 42 23 24
		f 4 15 48 -17 49
		f 4 16 17 -6 -26
		f 4 -8 -15 -16 18
		f 4 -20 10 -43 -49
		f 4 37 20 -37 -23
		f 4 71 243 112 -80
		f 4 64 65 -67 -22
		f 4 -1 35 -96 -65
		f 4 25 26 -42 -51
		f 4 28 27 40 41
		f 4 -29 85 86 87
		f 4 -27 -71 99 -86
		f 4 33 -3 34 -79
		f 4 84 -84 -36 -31
		f 3 242 43 44
		f 4 -35 -125 234 72
		f 4 31 32 240 239
		f 4 -45 -32 88 89
		f 4 45 -30 -33 -44
		f 4 238 -72 73 -69
		f 4 -9 -19 -50 50
		f 4 51 52 53 54
		f 4 55 56 57 -54
		f 4 58 59 -57 60
		f 4 135 -201 189 186
		f 4 136 -200 190 187
		f 4 123 74 -73 -63
		f 4 75 -66 -95 -98
		f 4 -70 76 -56 77
		f 4 78 -75 -62 -113
		f 4 -61 -77 -74 79
		f 4 -64 122 80 -124
		f 4 -59 61 -81 113
		f 4 96 81 245 -90
		f 4 82 83 -82 -126
		f 4 -89 90 -93 -97
		f 4 91 125 92 93
		f 4 -83 -92 94 95
		f 4 97 -94 98 117
		f 4 100 -100 -78 -53
		f 4 62 -68 -76 101
		f 4 -103 -87 -101 104
		f 4 105 120 139 -120
		f 4 126 121 140 -121
		f 4 -102 107 -106 63
		f 4 -107 108 -105 -52
		f 4 -109 110 111 -104
		f 4 115 -134 143 -122
		f 4 -91 -240 241 244
		f 4 -111 -116 118 -115
		f 4 -108 -118 -119 -127
		f 4 132 -114 -129 -143
		f 4 -136 133 106 -130
		f 4 -137 134 -58 -128
		f 4 -138 127 -60 -133
		f 4 -139 128 -123 119
		f 4 -142 129 -55 -135
		f 4 -157 -146 211 204
		f 4 -158 -147 212 202
		f 4 -159 -145 213 203
		f 4 -160 150 177 -156
		f 4 -161 151 178 165
		f 4 -162 152 179 -155
		f 4 -163 -167 180 167
		f 4 -164 -166 181 166
		f 4 -165 -168 182 -154
		f 4 156 155 -175 -152
		f 4 -176 -153 157 153
		f 4 -177 -151 158 154
		f 4 -178 168 191 -174
		f 4 -179 169 192 183
		f 4 -180 170 193 -173
		f 4 -181 -185 194 185
		f 4 -182 -184 195 184
		f 4 -183 -186 196 -172
		f 4 174 173 -189 -170
		f 4 -190 -171 175 171
		f 4 -191 -169 176 172
		f 4 -192 199 137 -202
		f 4 -193 197 138 130
		f 4 -188 -194 200 141
		f 4 -195 -199 -141 131
		f 4 -196 -131 -140 198
		f 4 -187 -197 -132 -144
		f 4 201 142 -198 188
		f 4 -205 -206 144 159
		f 4 -207 145 160 147
		f 4 -204 -208 146 161
		f 4 -209 -149 162 149
		f 4 -210 -148 163 148
		f 4 -203 -211 -150 164
		f 4 0 215 -217 -215
		f 4 -218 -216 21 229
		f 4 1 219 -221 -219
		f 4 2 222 -224 -222
		f 4 -226 -225 22 226
		f 4 3 218 -228 -227
		f 4 4 224 -229 -223
		f 4 30 214 -231 -220
		f 4 -39 231 232 -230
		f 4 124 221 -234 -232
		f 4 -235 38 66 67
		f 4 220 235 223 -237
		f 4 233 -236 230 237
		f 4 217 -233 -238 216
		f 4 227 236 228 225
		f 4 -25 -46 -21 -239
		f 4 -241 -40 -88 116
		f 4 -242 -117 102 103
		f 4 109 -4 36 -243
		f 4 -38 -5 -34 -244
		f 4 -112 114 -99 -245
		f 4 -246 -85 -2 -110
		f 4 -317 -316 -315 -252
		f 4 256 257 293 -253
		f 4 -293 286 -255 -254
		f 4 -294 259 292 -256
		f 4 269 -276 -259 -258
		f 4 -286 273 -260 258
		f 4 -266 252 255 -261
		f 4 -271 -270 -289 263
		f 4 -296 262 -295 -262
		f 4 271 251 -264 -263
		f 4 -265 261 260 253
		f 4 294 288 -257 265
		f 4 268 282 -267 -284
		f 4 325 -359 -490 -318
		f 4 267 312 -312 -311
		f 4 310 341 -282 246
		f 4 296 287 -273 -272
		f 4 -288 -287 -274 -275
		f 4 -334 -333 -332 274
		f 4 331 -346 316 272
		f 4 324 -281 248 -280
		f 4 276 281 329 -331
		f 3 -291 -290 -489
		f 4 -319 -481 370 280
		f 4 -486 -487 -279 -278
		f 4 -336 -335 277 290
		f 4 289 278 275 -292
		f 4 314 -320 317 -485
		f 4 -297 295 264 254
		f 4 -301 -300 -299 -298
		f 4 299 -304 -303 -302
		f 4 -307 302 -306 -305
		f 4 -433 -436 446 -382
		f 4 -434 -437 445 -383
		f 4 308 318 -321 -370
		f 4 343 340 311 -322
		f 4 -324 301 -323 315
		f 4 358 307 320 -325
		f 4 -326 319 322 306
		f 4 369 -327 -369 309
		f 4 -360 326 -308 304
		f 4 335 -492 -328 -343
		f 4 371 327 -330 -329
		f 4 342 338 -337 334
		f 4 -340 -339 -372 -338
		f 4 -342 -341 337 328
		f 4 -364 -345 339 -344
		f 4 298 323 345 -347
		f 4 -348 321 313 -309
		f 4 -351 346 332 348
		f 4 365 -386 -367 -352
		f 4 366 -387 -368 -373
		f 4 -310 351 -354 347
		f 4 297 350 -355 352
		f 4 349 -358 -357 354
		f 4 367 -390 379 -362
		f 4 -491 -488 485 336
		f 4 360 -365 361 356
		f 4 372 364 363 353
		f 4 388 374 359 -379
		f 4 375 -353 -380 381
		f 4 373 303 -381 382
		f 4 378 305 -374 383
		f 4 -366 368 -375 384
		f 4 380 300 -376 387
		f 4 -451 -458 391 402
		f 4 -449 -459 392 403
		f 4 -450 -460 390 404
		f 4 401 -424 -397 405
		f 4 -412 -425 -398 406
		f 4 400 -426 -399 407
		f 4 -414 -427 412 408
		f 4 -413 -428 411 409
		f 4 399 -429 413 410
		f 4 397 420 -402 -403
		f 4 -400 -404 398 421
		f 4 -401 -405 396 422
		f 4 419 -438 -415 423
		f 4 -430 -439 -416 424
		f 4 418 -440 -417 425
		f 4 -432 -441 430 426
		f 4 -431 -442 429 427
		f 4 417 -443 431 428
		f 4 415 434 -420 -421
		f 4 -418 -422 416 435
		f 4 -419 -423 414 436
		f 4 447 -384 -446 437
		f 4 -377 -385 -444 438
		f 4 -388 -447 439 433
		f 4 -378 386 444 440
		f 4 -445 385 376 441
		f 4 389 377 442 432
		f 4 -435 443 -389 -448
		f 4 -406 -391 451 450
		f 4 -394 -407 -392 452
		f 4 -408 -393 453 449
		f 4 -396 -409 394 454
		f 4 -395 -410 393 455
		f 4 -411 395 456 448
		f 4 460 462 -462 -247
		f 4 -476 -268 461 463
		f 4 464 466 -466 -248
		f 4 467 469 -469 -249
		f 4 -473 -269 470 471
		f 4 472 473 -465 -250
		f 4 468 474 -471 -251
		f 4 465 476 -461 -277
		f 4 475 -479 -478 284
		f 4 477 479 -468 -371
		f 4 -314 -313 -285 480
		f 4 482 -470 -482 -467
		f 4 -484 -477 481 -480
		f 4 -463 483 478 -464
		f 4 -472 -475 -483 -474
		f 4 484 266 291 270
		f 4 -363 333 285 486
		f 4 -350 -349 362 487
		f 4 488 -283 249 -356
		f 4 489 279 250 283
		f 4 490 344 -361 357
		f 4 355 247 330 491;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vs" 6;
createNode transform -n "mocap_pant_PLY" -p "mocap_geometry_GRP";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023C2";
	setAttr ".ove" yes;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode mesh -n "mocap_pant_PLYShape" -p "mocap_pant_PLY";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023C3";
	addAttr -ci true -sn "objectName" -ln "objectName" -dt "string";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ugsdt" no;
	setAttr ".vs" 6;
	setAttr ".vnm" 0;
	setAttr ".vcs" 2;
	setAttr -k on ".objectName" -type "string" "vipLowM1Pants2_PLYShape";
createNode mesh -n "mocap_pant_PLYShapeOrig" -p "mocap_pant_PLY";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023C4";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ugsdt" no;
	setAttr -s 160 ".vt[0:159]"  0 9.27723408 1.31849003 0 8.048853874 1.046210051
		 0 7.84610367 0.64385802 0 8.10176373 -0.67184901 0 9.46254444 -1.081439972 1.30648005 9.36239433 0.88002998
		 0.389065 7.98404408 1.057430029 0.123352 7.73847389 0.66803497 1.60754001 9.44320393 0.39529499
		 1.60882998 9.4978838 -0.12820201 0.36586601 8.064054489 -0.79075199 0.87615597 9.4578743 -1.023069978
		 0.43615499 9.45461369 -1.11479998 1.29787004 9.48034382 -0.68360299 0.58931798 5.48826981 0.79016298
		 0.292669 5.48789978 0.51182598 0.47576499 5.62222958 -0.59360802 0.85726202 5.67333984 -0.72335702
		 1.28303003 5.70028973 -0.62699598 1.56766999 5.68974018 -0.25892901 1.57894003 5.63389015 0.26143301
		 1.37476003 5.56406021 0.73722798 0.51748103 9.28211403 1.24863994 1.38115001 8.34203434 0.91027999
		 1.73986006 8.52254391 0.44077301 1.69271004 8.60116386 -0.226969 1.38069999 8.48429394 -0.69616002
		 0.89919901 8.30074406 -0.95083499 0.97484797 5.52237034 0.90714598 0.90579802 8.13921452 1.096670032
		 0.92775398 9.30881405 1.153 0 9.073583603 -1.069759965 0 8.3863945 1.26563001 0.46257001 8.41093445 1.20591998
		 0.92508 8.51824379 1.13848996 1.36670005 8.71931362 0.91126198 1.69526005 8.96470451 0.41482601
		 1.67216003 9.055873871 -0.157184 1.34765995 9.15808392 -0.694938 0.91952997 9.1359539 -1.040959954
		 0.44943401 9.081853867 -1.11661005 0.225463 5.57371044 -0.311093 0.11817 7.75717449 -0.36601201
		 0 7.85679436 -0.29969099 1.40962994 4.24225044 0.40595701 1.58359003 4.3613596 -0.066687003
		 1.049710035 4.11390018 0.63608098 0.304627 4.29078007 -0.33219099 0.70588702 4.10844994 0.53644401
		 0.51172602 4.3637104 -0.69204903 0.85464501 4.42313957 -0.90274203 1.28455997 4.46555996 -0.78038198
		 1.54904997 4.43855 -0.47751999 0.44667399 4.14741039 0.33930999 1.58307004 4.79059029 0.076765999
		 0.368 4.61190987 0.41423401 0.64523101 4.5891304 0.718503 1.28973997 4.8688097 -0.69313997
		 0.85194999 4.85647011 -0.83465397 0.465601 4.79706955 -0.66632497 1.0061000586 4.6188097 0.847592
		 0.314336 4.74442959 -0.29006201 1.55813003 4.85138035 -0.37472999 1.39137995 4.70654964 0.564951
		 1.0048600435 5.052280426 0.87166798 0.33638999 4.99026012 0.46300501 0.64415401 5.025420189 0.78642702
		 1.37545002 5.073220253 0.65981603 1.58194005 5.1323204 0.179015 1.29610002 5.1740799 -0.67646998
		 0.85137999 5.15769005 -0.80353999 0.472471 5.11264038 -0.60902399 1.56274998 5.17117977 -0.31309101
		 0.231088 5.079019547 -0.30221701 1.33500242 0.79999483 0.26778299 0.97832233 0.86412489 0.49469301
		 0.65128833 0.86471486 0.53022802 0.44926631 0.80350482 0.34159401 0.29876333 0.62488484 -0.36662
		 0.45988631 0.53406286 -0.835545 0.80707234 0.4844569 -1.037660003 1.27034235 0.47801191 -0.92007399
		 1.52128243 0.55066788 -0.57590503 1.57355237 0.66639483 -0.173776 -1.30648005 9.36239433 0.88002998
		 -0.389065 7.98404408 1.057430029 -0.123352 7.73847389 0.66803497 -1.60754001 9.44320393 0.39529499
		 -1.60882998 9.4978838 -0.12820201 -0.36586601 8.064054489 -0.79075199 -0.87615597 9.4578743 -1.023069978
		 -0.43615499 9.45461369 -1.11479998 -1.29787004 9.48034382 -0.68360299 -0.58931798 5.48826981 0.79016298
		 -0.292669 5.48789978 0.51182598 -0.47576499 5.62222958 -0.59360802 -0.85726202 5.67333984 -0.72335702
		 -1.28303003 5.70028973 -0.62699598 -1.56766999 5.68974018 -0.25892901 -1.57894003 5.63389015 0.26143301
		 -1.37476003 5.56406021 0.73722798 -0.51748103 9.28211403 1.24863994 -1.38115001 8.34203434 0.91027999
		 -1.73986006 8.52254391 0.44077301 -1.69271004 8.60116386 -0.226969 -1.38069999 8.48429394 -0.69616002
		 -0.89919901 8.30074406 -0.95083499 -0.97484797 5.52237034 0.90714598 -0.90579802 8.13921452 1.096670032
		 -0.92775398 9.30881405 1.153 -0.46257001 8.41093445 1.20591998 -0.92508 8.51824379 1.13848996
		 -1.36670005 8.71931362 0.91126198 -1.69526005 8.96470451 0.41482601 -1.67216003 9.055873871 -0.157184
		 -1.34765995 9.15808392 -0.694938 -0.91952997 9.1359539 -1.040959954 -0.44943401 9.081853867 -1.11661005
		 -0.225463 5.57371044 -0.311093 -0.11817 7.75717449 -0.36601201 -1.40962994 4.24225044 0.40595701
		 -1.58359003 4.3613596 -0.066687003 -1.049710035 4.11390018 0.63608098 -0.304627 4.29078007 -0.33219099
		 -0.70588702 4.10844994 0.53644401 -0.51172602 4.3637104 -0.69204903 -0.85464501 4.42313957 -0.90274203
		 -1.28455997 4.46555996 -0.78038198 -1.54904997 4.43855 -0.47751999 -0.44667399 4.14741039 0.33930999
		 -1.58307004 4.79059029 0.076765999 -0.368 4.61190987 0.41423401 -0.64523101 4.5891304 0.718503
		 -1.28973997 4.8688097 -0.69313997 -0.85194999 4.85647011 -0.83465397 -0.465601 4.79706955 -0.66632497
		 -1.0061000586 4.6188097 0.847592 -0.314336 4.74442959 -0.29006201 -1.55813003 4.85138035 -0.37472999
		 -1.39137995 4.70654964 0.564951 -1.0048600435 5.052280426 0.87166798 -0.33638999 4.99026012 0.46300501
		 -0.64415401 5.025420189 0.78642702 -1.37545002 5.073220253 0.65981603 -1.58194005 5.1323204 0.179015
		 -1.29610002 5.1740799 -0.67646998 -0.85137999 5.15769005 -0.80353999 -0.472471 5.11264038 -0.60902399
		 -1.56274998 5.17117977 -0.31309101 -0.231088 5.079019547 -0.30221701 -1.33500242 0.79999483 0.26778299
		 -0.97832233 0.86412489 0.49469301 -0.65128833 0.86471486 0.53022802 -0.44926631 0.80350482 0.34159401
		 -0.29876333 0.62488484 -0.36662 -0.45988631 0.53406286 -0.835545 -0.80707234 0.4844569 -1.037660003
		 -1.27034235 0.47801191 -0.92007399 -1.52128243 0.55066788 -0.57590503 -1.57355237 0.66639483 -0.173776;
	setAttr -s 303 ".ed";
	setAttr ".ed[0:165]"  41 15 1 15 14 1 14 28 1 56 66 1 66 65 1 65 55 1 55 56 1
		 14 66 1 66 64 1 64 28 1 47 49 1 48 53 1 46 48 1 21 20 1 20 19 1 68 20 1 21 67 1 67 68 1
		 22 0 0 0 32 1 6 1 1 1 2 1 2 7 1 7 6 1 2 43 1 8 5 0 5 35 1 17 16 1 16 41 1 50 49 1
		 49 59 1 59 58 1 58 50 1 19 18 1 18 17 1 51 50 1 58 57 1 57 51 1 52 45 1 40 12 1 12 11 0
		 11 39 1 39 40 1 3 10 1 10 42 1 42 43 1 43 3 1 40 31 1 31 4 1 4 12 0 11 13 0 13 38 1
		 38 39 1 30 22 0 32 33 1 33 22 1 33 34 1 34 30 1 35 36 1 36 8 1 9 8 0 36 37 1 37 9 1
		 25 26 1 26 27 1 27 10 1 3 31 1 13 9 0 37 38 1 45 44 1 60 46 1 46 44 1 44 63 1 63 60 1
		 21 28 1 64 67 1 34 35 1 5 30 0 79 80 0 76 77 0 82 83 0 80 81 0 65 15 1 16 71 1 71 73 1
		 73 41 1 17 70 1 70 71 1 18 69 1 69 70 1 19 72 1 72 69 1 32 1 1 6 33 1 6 29 1 29 34 1
		 29 23 1 23 35 1 23 24 1 24 36 1 24 25 1 25 37 1 26 38 1 27 39 1 10 40 1 53 47 1 73 65 1
		 7 42 1 51 52 1 68 72 1 78 79 0 75 76 0 74 75 0 83 74 0 81 82 0 77 78 0 60 56 1 56 48 1
		 57 62 1 62 52 1 54 62 1 62 72 1 68 54 1 45 54 1 54 63 1 55 53 1 47 61 1 61 59 1 55 61 1
		 63 67 1 64 60 1 61 73 1 71 59 1 57 69 1 70 58 1 46 75 1 74 44 1 48 76 1 53 77 1 47 78 1
		 49 79 1 50 80 1 51 81 1 52 82 1 45 83 1 6 14 1 28 29 1 21 23 1 20 24 1 19 25 1 18 26 1
		 17 27 1 16 10 1 41 42 1 15 7 1 93 94 1 107 93 1 132 131 1 131 141 1 141 142 1 142 132 1
		 107 140 1 140 142 1 142 93 1 125 123 1 129 124 1;
	setAttr ".ed[166:302]" 124 122 1 99 100 1 98 99 1 144 143 1 143 100 1 99 144 1
		 0 101 0 85 86 1 86 2 1 1 85 1 86 119 1 84 87 0 95 96 1 118 95 1 126 134 1 134 135 1
		 135 125 1 125 126 1 97 98 1 96 97 1 127 133 1 133 134 1 126 127 1 121 128 1 117 116 1
		 116 90 1 90 91 0 91 117 1 43 119 1 119 89 1 89 3 1 91 4 0 31 117 1 116 115 1 115 92 1
		 92 90 0 109 111 1 101 109 0 101 110 1 110 32 1 111 110 1 87 113 1 113 112 1 112 84 1
		 88 114 1 114 113 1 87 88 0 105 104 1 106 105 1 89 106 1 115 114 1 88 92 0 120 121 1
		 136 139 1 139 120 1 120 122 1 122 136 1 143 140 1 107 100 1 112 111 1 109 84 0 156 155 0
		 153 152 0 159 158 0 157 156 0 94 141 1 141 149 1 118 149 1 149 147 1 147 95 1 147 146 1
		 146 96 1 146 145 1 145 97 1 145 148 1 148 98 1 110 85 1 111 108 1 108 85 1 112 102 1
		 102 108 1 113 103 1 103 102 1 114 104 1 104 103 1 115 105 1 116 106 1 117 89 1 118 94 1
		 128 127 1 148 144 1 156 126 1 155 154 0 152 151 0 151 150 0 150 159 0 154 153 0 158 157 0
		 123 129 1 124 132 1 132 136 1 128 138 1 138 133 1 130 144 1 148 138 1 138 130 1 139 130 1
		 130 121 1 129 131 1 135 137 1 137 123 1 137 131 1 136 140 1 143 139 1 135 147 1 149 137 1
		 145 133 1 134 146 1 120 150 1 151 122 1 152 124 1 153 129 1 154 123 1 155 125 1 157 127 1
		 158 128 1 159 121 1 108 107 1 93 85 1 102 100 1 103 99 1 104 98 1 105 97 1 106 96 1
		 89 95 1 119 118 1 86 94 1;
	setAttr -s 160 ".n[0:159]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20;
	setAttr -s 142 -ch 568 ".fc[0:141]" -type "polyFaces" 
		f 4 12 137 -112 -136
		f 4 69 -137 -114 -145
		f 4 1 -146 -24 -155
		f 4 2 146 -95 145
		f 4 3 4 5 6
		f 4 -3 7 8 9
		f 4 11 138 -80 -138
		f 4 13 148 -99 -148
		f 4 14 149 -101 -149
		f 4 15 -14 16 17
		f 4 18 19 54 55
		f 4 20 21 22 23
		f 4 -23 24 -46 -108
		f 4 25 26 58 59
		f 4 10 140 -111 -140
		f 4 28 153 -45 -153
		f 4 27 152 -66 -152
		f 4 29 30 31 32
		f 4 -30 141 -79 -141
		f 4 33 150 -64 -150
		f 4 34 151 -65 -151
		f 4 35 -33 36 37
		f 4 38 144 -81 -144
		f 4 -36 142 -82 -142
		f 4 39 40 41 42
		f 4 43 44 45 46
		f 4 -40 47 48 49
		f 4 -42 50 51 52
		f 4 53 -56 56 57
		f 4 60 -60 61 62
		f 4 63 102 -69 -102
		f 4 64 103 -53 -103
		f 4 65 104 -43 -104
		f 4 -44 66 -48 -105
		f 4 67 -63 68 -52
		f 4 -72 135 -113 136
		f 4 70 71 72 73
		f 4 74 -10 75 -17
		f 4 -75 147 -97 -147
		f 4 -58 76 -27 77
		f 4 82 -1 -86 106
		f 4 -29 83 84 85
		f 4 -28 86 87 -84
		f 4 -35 88 89 -87
		f 4 -89 -34 90 91
		f 4 -55 92 -21 93
		f 4 -57 -94 94 95
		f 4 -77 -96 96 97
		f 4 -59 -98 98 99
		f 4 -62 -100 100 101
		f 4 107 -154 0 154
		f 4 108 143 -115 -143
		f 4 -15 -16 109 -91
		f 4 -116 -139 105 139
		f 4 -13 -71 116 117
		f 4 118 119 -109 -38
		f 4 120 121 -110 122
		f 4 -70 123 124 -73
		f 4 -12 -118 -7 125
		f 4 -11 126 127 -31
		f 4 -127 -106 -126 128
		f 4 129 -76 130 -74
		f 4 -128 131 -85 132
		f 4 -119 133 -92 -122
		f 4 -121 -124 -39 -120
		f 4 -125 -123 -18 -130
		f 4 -5 -8 -2 -83
		f 4 -9 -4 -117 -131
		f 4 -129 -6 -107 -132
		f 4 -88 134 -32 -133
		f 4 -90 -134 -37 -135
		f 4 166 -286 -260 286
		f 4 218 -293 -262 -285
		f 4 155 -303 -174 -295
		f 4 156 294 -245 293
		f 4 157 158 159 160
		f 4 161 162 163 -157
		f 4 165 -287 -229 287
		f 4 167 -296 -249 296
		f 4 168 -297 -251 297
		f 4 169 170 -168 171
		f 4 -20 172 204 205
		f 4 173 174 -22 175
		f 4 -25 -175 176 -195
		f 4 177 207 208 209
		f 4 164 -289 -259 289
		f 4 179 -301 -196 301
		f 4 178 -300 -216 300
		f 4 180 181 182 183
		f 4 -184 -290 -228 257
		f 4 184 -298 -214 298
		f 4 185 -299 -215 299
		f 4 186 187 -181 188
		f 4 189 -292 -230 292
		f 4 -189 -258 -231 290
		f 4 190 191 192 193
		f 4 -47 194 195 196
		f 4 197 -49 198 -194
		f 4 199 200 201 -192
		f 4 203 202 206 -205
		f 4 210 211 -208 212
		f 4 213 -250 -217 251
		f 4 214 -252 -200 252
		f 4 215 -253 -191 253
		f 4 -67 -197 -254 -199
		f 4 -201 216 -211 217
		f 4 -222 284 -261 285
		f 4 219 220 221 222
		f 4 -171 223 -162 224
		f 4 -225 -294 -247 295
		f 4 -210 225 -203 226
		f 4 231 232 -234 254
		f 4 233 234 235 -180
		f 4 -236 236 237 -179
		f 4 -238 238 239 -186
		f 4 240 241 -185 -240
		f 4 242 -176 -93 -206
		f 4 243 244 -243 -207
		f 4 245 246 -244 -226
		f 4 247 248 -246 -209
		f 4 249 250 -248 -212
		f 4 -255 -302 -177 302
		f 4 255 -291 -264 291
		f 4 -242 256 -172 -169
		f 4 264 -288 -263 288
		f 4 265 266 -223 -167
		f 4 -187 -256 267 268
		f 4 269 -257 270 271
		f 4 -221 272 273 -219
		f 4 274 -158 -266 -166
		f 4 -183 275 276 -165
		f 4 -277 277 -275 -265
		f 4 -220 278 -224 279
		f 4 280 -235 281 -276
		f 4 -271 -241 282 -269
		f 4 -268 -190 -274 -272
		f 4 -280 -170 -270 -273
		f 4 -232 -156 -164 -160
		f 4 -279 -267 -161 -163
		f 4 -233 -159 -278 -282
		f 4 -281 -182 283 -237
		f 4 -284 -188 -283 -239;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vs" 6;
	setAttr ".vnm" 0;
createNode transform -n "mocap_shoe_L_PLY" -p "mocap_geometry_GRP";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023C5";
	setAttr ".ove" yes;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode mesh -n "mocap_shoe_L_PLYShape" -p "mocap_shoe_L_PLY";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023C6";
	addAttr -ci true -sn "objectName" -ln "objectName" -dt "string";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ugsdt" no;
	setAttr ".vs" 6;
	setAttr ".bw" 3;
	setAttr ".vnm" 0;
	setAttr ".vcs" 2;
	setAttr -k on ".objectName" -type "string" "vipLowM1Shoes1_PLYShape";
createNode mesh -n "mocap_shoe_L_PLYShapeOrig" -p "mocap_shoe_L_PLY";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023C7";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ugsdt" no;
	setAttr -s 26 ".vt[0:25]"  1.091168523 0.45875424 1.81238854 1.38262928 0.44261909 1.34275663
		 1.05298543 0.54172969 1.3647579 1.082311153 0.54228652 -0.80295253 1.023287416 0.87407386 -0.67085689
		 0.73627263 0.55311769 -0.98666692 0.71852708 0.96075535 -0.82866257 1.084972501 0.98555005 0.054517951
		 1.29168355 0.45765918 0.25795263 0.78876561 1.13899708 0.20060246 1.087693691 0.053444251 -0.83187473
		 0.74244976 0.1018326 -0.95054603 1.31591082 -0.034948103 0.21187769 1.55073702 -0.026313253 1.29023445
		 1.10579205 0.070908889 1.85054386 0.35640842 -0.0072085783 -0.71254605 0.41861272 0.51866996 -0.73771769
		 0.51283842 0.49118447 0.33817807 0.64062715 -0.040620908 0.38268182 0.58829248 -0.031361669 1.42695034
		 0.6953584 0.44386029 1.42702925 0.56108016 0.9762063 0.12362985 0.49794203 0.88441539 -0.6205771
		 1.079927444 -0.093008786 1.33965468 0.94022214 -0.072076477 0.3201519 0.87718761 0.77970111 0.59019071;
	setAttr -s 48 ".ed[0:47]"  1 0 1 2 1 1 2 25 1 4 3 1 3 8 1 7 4 0 5 3 1
		 4 6 0 6 5 1 8 7 1 9 7 0 8 1 1 3 10 1 10 12 1 5 11 1 11 10 1 12 8 1 12 13 1 13 1 1
		 13 14 1 14 0 1 15 11 1 5 16 1 16 15 1 16 17 1 17 18 1 18 15 1 17 20 1 14 19 1 19 20 1
		 20 0 1 19 18 1 2 20 1 17 21 1 22 21 0 21 9 0 6 22 0 22 16 1 14 23 1 13 23 1 23 19 1
		 23 24 1 12 24 1 24 18 1 24 11 1 25 9 1 8 25 1 25 17 1;
	setAttr -s 26 ".n[0:25]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20;
	setAttr -s 23 -ch 90 ".fc[0:22]" -type "polyFaces" 
		f 4 32 30 -1 -2
		f 4 -10 -5 -4 -6
		f 4 -9 -8 3 -7
		f 4 -3 1 -12 46
		f 4 -17 -14 -13 4
		f 4 12 -16 -15 6
		f 4 11 -19 -18 16
		f 4 0 -21 -20 18
		f 4 -24 -23 14 -22
		f 4 -27 -26 -25 23
		f 4 -31 -30 -29 20
		f 4 -28 25 -32 29
		f 4 47 27 -33 2
		f 4 22 -38 -37 8
		f 4 33 -35 37 24
		f 4 13 42 44 15
		f 4 39 41 -43 17
		f 3 38 -40 19
		f 4 -45 43 26 21
		f 3 -41 -39 28
		f 4 -44 -42 40 31
		f 4 -46 -47 9 -11
		f 4 -36 -34 -48 45;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vs" 6;
	setAttr ".bw" 3;
	setAttr ".vnm" 0;
createNode transform -n "mocap_shoe_R_PLY" -p "mocap_geometry_GRP";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023C8";
	setAttr ".ove" yes;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode mesh -n "mocap_shoe_R_PLYShape" -p "mocap_shoe_R_PLY";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023C9";
	addAttr -ci true -sn "objectName" -ln "objectName" -dt "string";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ugsdt" no;
	setAttr ".vs" 6;
	setAttr ".bw" 3;
	setAttr ".vnm" 0;
	setAttr ".vcs" 2;
	setAttr -k on ".objectName" -type "string" "vipLowM1Shoes1_PLYShape";
createNode mesh -n "mocap_shoe_R_PLYShapeOrig" -p "mocap_shoe_R_PLY";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023CA";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ugsdt" no;
	setAttr -s 26 ".vt[0:25]"  -1.091168523 0.45875424 1.81238854 -1.38262928 0.44261909 1.34275663
		 -1.05298543 0.54172969 1.3647579 -1.082311153 0.54228652 -0.80295253 -1.023287416 0.87407386 -0.67085689
		 -0.73627263 0.55311769 -0.98666692 -0.71852708 0.96075535 -0.82866257 -1.084972501 0.98555005 0.054517951
		 -1.29168355 0.45765918 0.25795263 -0.78876561 1.13899708 0.20060246 -1.087693691 0.053444251 -0.83187473
		 -0.74244976 0.1018326 -0.95054603 -1.31591082 -0.034948103 0.21187769 -1.55073702 -0.026313253 1.29023445
		 -1.10579205 0.070908889 1.85054386 -0.35640842 -0.0072085783 -0.71254605 -0.41861272 0.51866996 -0.73771769
		 -0.51283842 0.49118447 0.33817807 -0.64062715 -0.040620908 0.38268182 -0.58829248 -0.031361669 1.42695034
		 -0.6953584 0.44386029 1.42702925 -0.56108016 0.9762063 0.12362985 -0.49794203 0.88441539 -0.6205771
		 -1.079927444 -0.093008786 1.33965468 -0.94022214 -0.072076477 0.3201519 -0.87718761 0.77970111 0.59019071;
	setAttr -s 48 ".ed[0:47]"  1 0 1 2 1 1 2 25 1 4 3 1 3 8 1 7 4 0 5 3 1
		 4 6 0 6 5 1 8 7 1 9 7 0 8 1 1 3 10 1 10 12 1 5 11 1 11 10 1 12 8 1 12 13 1 13 1 1
		 13 14 1 14 0 1 15 11 1 5 16 1 16 15 1 16 17 1 17 18 1 18 15 1 17 20 1 14 19 1 19 20 1
		 20 0 1 19 18 1 2 20 1 17 21 1 22 21 0 21 9 0 6 22 0 22 16 1 14 23 1 13 23 1 23 19 1
		 23 24 1 12 24 1 24 18 1 24 11 1 25 9 1 8 25 1 25 17 1;
	setAttr -s 26 ".n[0:25]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20;
	setAttr -s 23 -ch 90 ".fc[0:22]" -type "polyFaces" 
		f 4 1 0 -31 -33
		f 4 5 3 4 9
		f 4 6 -4 7 8
		f 4 -47 11 -2 2
		f 4 -5 12 13 16
		f 4 -7 14 15 -13
		f 4 -17 17 18 -12
		f 4 -19 19 20 -1
		f 4 21 -15 22 23
		f 4 -24 24 25 26
		f 4 -21 28 29 30
		f 4 -30 31 -26 27
		f 4 -3 32 -28 -48
		f 4 -9 36 37 -23
		f 4 -25 -38 34 -34
		f 4 -16 -45 -43 -14
		f 4 -18 42 -42 -40
		f 3 -20 39 -39
		f 4 -22 -27 -44 44
		f 3 -29 38 40
		f 4 -32 -41 41 43
		f 4 10 -10 46 45
		f 4 -46 47 33 35;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vs" 6;
	setAttr ".bw" 3;
	setAttr ".vnm" 0;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023CB";
	setAttr -s 10 ".lnk";
	setAttr -s 9 ".slnk";
createNode displayLayerManager -n "layerManager";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023CC";
	setAttr ".cdl" 1;
	setAttr -s 2 ".dli[1]"  1;
createNode displayLayer -n "defaultLayer";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023CD";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023CE";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023CF";
	setAttr ".g" yes;
createNode mentalrayItemsList -s -n "mentalrayItemsList";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023D0";
createNode mentalrayGlobals -s -n "mentalrayGlobals";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023D1";
createNode mentalrayOptions -s -n "miDefaultOptions";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023D2";
	addAttr -ci true -m -sn "stringOptions" -ln "stringOptions" -at "compound" -nc 
		3;
	addAttr -ci true -sn "name" -ln "name" -dt "string" -p "stringOptions";
	addAttr -ci true -sn "value" -ln "value" -dt "string" -p "stringOptions";
	addAttr -ci true -sn "type" -ln "type" -dt "string" -p "stringOptions";
	setAttr -s 45 ".stringOptions";
	setAttr ".stringOptions[0].name" -type "string" "rast motion factor";
	setAttr ".stringOptions[0].value" -type "string" "1.0";
	setAttr ".stringOptions[0].type" -type "string" "scalar";
	setAttr ".stringOptions[1].name" -type "string" "rast transparency depth";
	setAttr ".stringOptions[1].value" -type "string" "8";
	setAttr ".stringOptions[1].type" -type "string" "integer";
	setAttr ".stringOptions[2].name" -type "string" "rast useopacity";
	setAttr ".stringOptions[2].value" -type "string" "true";
	setAttr ".stringOptions[2].type" -type "string" "boolean";
	setAttr ".stringOptions[3].name" -type "string" "importon";
	setAttr ".stringOptions[3].value" -type "string" "false";
	setAttr ".stringOptions[3].type" -type "string" "boolean";
	setAttr ".stringOptions[4].name" -type "string" "importon density";
	setAttr ".stringOptions[4].value" -type "string" "1.0";
	setAttr ".stringOptions[4].type" -type "string" "scalar";
	setAttr ".stringOptions[5].name" -type "string" "importon merge";
	setAttr ".stringOptions[5].value" -type "string" "0.0";
	setAttr ".stringOptions[5].type" -type "string" "scalar";
	setAttr ".stringOptions[6].name" -type "string" "importon trace depth";
	setAttr ".stringOptions[6].value" -type "string" "0";
	setAttr ".stringOptions[6].type" -type "string" "integer";
	setAttr ".stringOptions[7].name" -type "string" "importon traverse";
	setAttr ".stringOptions[7].value" -type "string" "true";
	setAttr ".stringOptions[7].type" -type "string" "boolean";
	setAttr ".stringOptions[8].name" -type "string" "shadowmap pixel samples";
	setAttr ".stringOptions[8].value" -type "string" "3";
	setAttr ".stringOptions[8].type" -type "string" "integer";
	setAttr ".stringOptions[9].name" -type "string" "ambient occlusion";
	setAttr ".stringOptions[9].value" -type "string" "false";
	setAttr ".stringOptions[9].type" -type "string" "boolean";
	setAttr ".stringOptions[10].name" -type "string" "ambient occlusion rays";
	setAttr ".stringOptions[10].value" -type "string" "256";
	setAttr ".stringOptions[10].type" -type "string" "integer";
	setAttr ".stringOptions[11].name" -type "string" "ambient occlusion cache";
	setAttr ".stringOptions[11].value" -type "string" "false";
	setAttr ".stringOptions[11].type" -type "string" "boolean";
	setAttr ".stringOptions[12].name" -type "string" "ambient occlusion cache density";
	setAttr ".stringOptions[12].value" -type "string" "1.0";
	setAttr ".stringOptions[12].type" -type "string" "scalar";
	setAttr ".stringOptions[13].name" -type "string" "ambient occlusion cache points";
	setAttr ".stringOptions[13].value" -type "string" "64";
	setAttr ".stringOptions[13].type" -type "string" "integer";
	setAttr ".stringOptions[14].name" -type "string" "irradiance particles";
	setAttr ".stringOptions[14].value" -type "string" "false";
	setAttr ".stringOptions[14].type" -type "string" "boolean";
	setAttr ".stringOptions[15].name" -type "string" "irradiance particles rays";
	setAttr ".stringOptions[15].value" -type "string" "256";
	setAttr ".stringOptions[15].type" -type "string" "integer";
	setAttr ".stringOptions[16].name" -type "string" "irradiance particles interpolate";
	setAttr ".stringOptions[16].value" -type "string" "1";
	setAttr ".stringOptions[16].type" -type "string" "integer";
	setAttr ".stringOptions[17].name" -type "string" "irradiance particles interppoints";
	setAttr ".stringOptions[17].value" -type "string" "64";
	setAttr ".stringOptions[17].type" -type "string" "integer";
	setAttr ".stringOptions[18].name" -type "string" "irradiance particles indirect passes";
	setAttr ".stringOptions[18].value" -type "string" "0";
	setAttr ".stringOptions[18].type" -type "string" "integer";
	setAttr ".stringOptions[19].name" -type "string" "irradiance particles scale";
	setAttr ".stringOptions[19].value" -type "string" "1.0";
	setAttr ".stringOptions[19].type" -type "string" "scalar";
	setAttr ".stringOptions[20].name" -type "string" "irradiance particles env";
	setAttr ".stringOptions[20].value" -type "string" "true";
	setAttr ".stringOptions[20].type" -type "string" "boolean";
	setAttr ".stringOptions[21].name" -type "string" "irradiance particles env rays";
	setAttr ".stringOptions[21].value" -type "string" "256";
	setAttr ".stringOptions[21].type" -type "string" "integer";
	setAttr ".stringOptions[22].name" -type "string" "irradiance particles env scale";
	setAttr ".stringOptions[22].value" -type "string" "1";
	setAttr ".stringOptions[22].type" -type "string" "integer";
	setAttr ".stringOptions[23].name" -type "string" "irradiance particles rebuild";
	setAttr ".stringOptions[23].value" -type "string" "true";
	setAttr ".stringOptions[23].type" -type "string" "boolean";
	setAttr ".stringOptions[24].name" -type "string" "irradiance particles file";
	setAttr ".stringOptions[24].value" -type "string" "";
	setAttr ".stringOptions[24].type" -type "string" "string";
	setAttr ".stringOptions[25].name" -type "string" "geom displace motion factor";
	setAttr ".stringOptions[25].value" -type "string" "1.0";
	setAttr ".stringOptions[25].type" -type "string" "scalar";
	setAttr ".stringOptions[26].name" -type "string" "contrast all buffers";
	setAttr ".stringOptions[26].value" -type "string" "true";
	setAttr ".stringOptions[26].type" -type "string" "boolean";
	setAttr ".stringOptions[27].name" -type "string" "finalgather normal tolerance";
	setAttr ".stringOptions[27].value" -type "string" "25.842";
	setAttr ".stringOptions[27].type" -type "string" "scalar";
	setAttr ".stringOptions[28].name" -type "string" "trace camera clip";
	setAttr ".stringOptions[28].value" -type "string" "false";
	setAttr ".stringOptions[28].type" -type "string" "boolean";
	setAttr ".stringOptions[29].name" -type "string" "unified sampling";
	setAttr ".stringOptions[29].value" -type "string" "true";
	setAttr ".stringOptions[29].type" -type "string" "boolean";
	setAttr ".stringOptions[30].name" -type "string" "samples quality";
	setAttr ".stringOptions[30].value" -type "string" "0.25 0.25 0.25 0.25";
	setAttr ".stringOptions[30].type" -type "string" "color";
	setAttr ".stringOptions[31].name" -type "string" "samples min";
	setAttr ".stringOptions[31].value" -type "string" "1.0";
	setAttr ".stringOptions[31].type" -type "string" "scalar";
	setAttr ".stringOptions[32].name" -type "string" "samples max";
	setAttr ".stringOptions[32].value" -type "string" "100.0";
	setAttr ".stringOptions[32].type" -type "string" "scalar";
	setAttr ".stringOptions[33].name" -type "string" "samples error cutoff";
	setAttr ".stringOptions[33].value" -type "string" "0.0 0.0 0.0 0.0";
	setAttr ".stringOptions[33].type" -type "string" "color";
	setAttr ".stringOptions[34].name" -type "string" "samples per object";
	setAttr ".stringOptions[34].value" -type "string" "false";
	setAttr ".stringOptions[34].type" -type "string" "boolean";
	setAttr ".stringOptions[35].name" -type "string" "progressive";
	setAttr ".stringOptions[35].value" -type "string" "false";
	setAttr ".stringOptions[35].type" -type "string" "boolean";
	setAttr ".stringOptions[36].name" -type "string" "progressive max time";
	setAttr ".stringOptions[36].value" -type "string" "0";
	setAttr ".stringOptions[36].type" -type "string" "integer";
	setAttr ".stringOptions[37].name" -type "string" "progressive subsampling size";
	setAttr ".stringOptions[37].value" -type "string" "1";
	setAttr ".stringOptions[37].type" -type "string" "integer";
	setAttr ".stringOptions[38].name" -type "string" "iray";
	setAttr ".stringOptions[38].value" -type "string" "false";
	setAttr ".stringOptions[38].type" -type "string" "boolean";
	setAttr ".stringOptions[39].name" -type "string" "light relative scale";
	setAttr ".stringOptions[39].value" -type "string" "0.31831";
	setAttr ".stringOptions[39].type" -type "string" "scalar";
	setAttr ".stringOptions[40].name" -type "string" "trace camera motion vectors";
	setAttr ".stringOptions[40].value" -type "string" "false";
	setAttr ".stringOptions[40].type" -type "string" "boolean";
	setAttr ".stringOptions[41].name" -type "string" "ray differentials";
	setAttr ".stringOptions[41].value" -type "string" "true";
	setAttr ".stringOptions[41].type" -type "string" "boolean";
	setAttr ".stringOptions[42].name" -type "string" "environment lighting mode";
	setAttr ".stringOptions[42].value" -type "string" "off";
	setAttr ".stringOptions[42].type" -type "string" "string";
	setAttr ".stringOptions[43].name" -type "string" "environment lighting quality";
	setAttr ".stringOptions[43].value" -type "string" "0.167";
	setAttr ".stringOptions[43].type" -type "string" "scalar";
	setAttr ".stringOptions[44].name" -type "string" "environment lighting shadow";
	setAttr ".stringOptions[44].value" -type "string" "transparent";
	setAttr ".stringOptions[44].type" -type "string" "string";
createNode mentalrayFramebuffer -s -n "miDefaultFramebuffer";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023D3";
createNode shadingEngine -n "lambert2SG";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023D4";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo1";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023D5";
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023D6";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 24 -ast 1 -aet 48 ";
	setAttr ".st" 6;
createNode shadingEngine -n "initialShadingGroup1";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023D7";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo3";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023D8";
createNode script -n "uiConfigurationScriptNode";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023F4";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n"
		+ "            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n"
		+ "            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n"
		+ "            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n"
		+ "            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n"
		+ "            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n"
		+ "            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n"
		+ "        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n"
		+ "            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n"
		+ "            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n"
		+ "            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1249\n            -height 813\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 1\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n"
		+ "            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 0\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n"
		+ "            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n"
		+ "                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n"
		+ "\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -showCurveNames 0\n                -showActiveCurveNames 0\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                -valueLinesToggle 0\n"
		+ "                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n"
		+ "                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n"
		+ "                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n"
		+ "                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n"
		+ "                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -keyReleaseCommand \"nodeEdKeyReleaseCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n"
		+ "                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab 0\n                -editorMode \"default\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"blendShapePanel\" (localizedPanelLabel(\"Blend Shape\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tblendShapePanel -edit -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n"
		+ "            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"0\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n"
		+ "            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1249\\n    -height 813\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1249\\n    -height 813\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode shadingEngine -n "lambert2SG1";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023F5";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo4";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023F6";
createNode shadingEngine -n "initialShadingGroup2";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023F7";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo5";
	rename -uid "D3D318C0-0000-1586-5B67-E791000023F8";
createNode shadingEngine -n "lambert2SG2";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002414";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo6";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002415";
createNode shadingEngine -n "initialShadingGroup3";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002416";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo7";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002417";
createNode dagPose -n "bindPose1";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002433";
	setAttr -s 31 ".wm";
	setAttr -s 46 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0
		 8.9231745720989668 -0.17376929722515433 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0.5 0.49999999999999994 0.5 0.50000000000000011 1
		 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 0
		 -2.2204460492503131e-16 1 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 1 0 6.123233995736766e-17 1
		 1 1 yes;
	setAttr ".xm[2]" -type "matrix" "xform" 1 1 1 0 0 0 0 4.2716684427277309
		 2.7755575615628914e-17 -1.8873791418627657e-15 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[3]" -type "matrix" "xform" 1 1 1 0 0 0 0 3.8601122635449254
		 3.6082248300317583e-16 -1.1102230246251563e-16 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 4.9460565984978505e-10 3.3940520778679829e-07 0.51019127719243595 0.86006096334889892 1
		 1 1 yes;
	setAttr ".xm[4]" -type "matrix" "xform" 1 1 1 0 0 0 0 1.3684725807972993
		 -5.5511151231257827e-16 -2.653335551272562e-09 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 -1.2785578526999439e-16 -1.8023068273223423e-07 0.24739522761289695 0.96891465122286724 1
		 1 1 yes;
	setAttr ".xm[5]" -type "matrix" "xform" 1 1 1 0 0 0 0 0.86637208112808017
		 2.2204460492503131e-16 4.4408920985006262e-16 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[6]" -type "matrix" "xform" 1 1 1 0 0 0 0 -4.5720989660935629e-06
		 2.972251545441118e-07 -1 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 -1 0 0 6.123233995736766e-17 1
		 1 1 yes;
	setAttr ".xm[7]" -type "matrix" "xform" 1 1 1 0 0 0 0 -4.2716600000000007
		 0 -8.8817841970012523e-16 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[8]" -type "matrix" "xform" 1 1 1 0 0 0 0 -3.860116000000001
		 0 -8.8817841970012523e-16 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 2.6469779601696897e-23 3.3911180559673054e-07 0.5101912771924364 0.86006096334889859 1
		 1 1 yes;
	setAttr ".xm[9]" -type "matrix" "xform" 1 1 1 0 0 0 0 -1.3684721155956827
		 1.8731120976500648e-07 2.0175146686618461e-07 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 7.218976700476308e-09 -1.7867198974451593e-07 0.24739522761289776 0.96891465122286724 1
		 1 1 yes;
	setAttr ".xm[10]" -type "matrix" "xform" 1 1 1 0 0 0 0 -0.86636999999999986
		 1.9428902930940239e-15 3.2782812020570873e-09 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[11]" -type "matrix" "xform" 1 1 1 0 0 0 0 0.58774894329774696
		 0 -1.3050648190965283e-16 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[12]" -type "matrix" "xform" 1 1 1 0 0 0 0 0.9893001566856352
		 0 -2.1966876244353344e-16 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[13]" -type "matrix" "xform" 1 1 1 0 0 0 0 1.2035565681447071
		 0 -2.6724324267861797e-16 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[14]" -type "matrix" "xform" 1 1 1 0 0 0 0 1.1721460718394212
		 0 -2.6026871143601165e-16 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[15]" -type "matrix" "xform" 1 1 1 0 0 0 0 1.0527813315795027
		 -7.4940054162198066e-16 -2.337644148430199e-16 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[16]" -type "matrix" "xform" 1 1 1 0 0 0 0 1.4094567464894061
		 0 -3.1296226643316053e-16 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[17]" -type "matrix" "xform" 1 1 1 0 0 0 0 1.7042113670357055
		 0 -3.9443045261050617e-31 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[18]" -type "matrix" "xform" 1 1 1 0 0 0 0 0.65167368793352054
		 2.9722515418328932e-07 0.6441929999999999 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 -0.5 -0.5 -0.49999999999999994 0.50000000000000011 1
		 1 1 yes;
	setAttr ".xm[19]" -type "matrix" "xform" 1 1 1 0 0 0 0 0.97086700000000004
		 -0.014999999999998792 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[20]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.8141100000000008
		 3.5527136788005009e-15 -5.5511151231257827e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[21]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.5164999999999997
		 0 -2.7755575615628914e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[22]" -type "matrix" "xform" 1 1 1 0 0 0 0 0.82956999999999947
		 0 2.7755575615628914e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[23]" -type "matrix" "xform" 1 1 1 0 0 0 0 0.93052999999999919
		 -0.40000000000000002 -2.7755575615628914e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[24]" -type "matrix" "xform" 1 1 1 0 0 0 0 0.65167368793352054
		 2.9722515446084508e-07 -0.64419300000000013 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0.50000000000000011 -0.49999999999999994 0.5 0.5 1
		 1 1 yes;
	setAttr ".xm[25]" -type "matrix" "xform" 1 1 1 0 0 0 0 -0.97086700000000004
		 0.014999999999998792 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[26]" -type "matrix" "xform" 1 1 1 0 0 0 0 -2.8141100000000008
		 -3.5527136788005009e-15 5.5511151231257827e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[27]" -type "matrix" "xform" 1 1 1 0 0 0 0 -2.5164999999999997
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[28]" -type "matrix" "xform" 1 1 1 0 0 0 0 -0.82956999999999947
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[29]" -type "matrix" "xform" 1 1 1 0 0 0 0 0.86637208112808017
		 2.2204460492503131e-16 4.4408920985006262e-16 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[30]" -type "matrix" "xform" 1 1 1 0 0 0 0 -0.86636999999999986
		 1.9428902930940239e-15 3.2782812020570873e-09 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[31]" -type "matrix" "xform" 1 1 1 0 0 0 0 1.7042113670357055
		 0 -3.9443045261050617e-31 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[32]" -type "matrix" "xform" 1 1 1 0 0 0 0 0.93052999999999919
		 -0.40000000000000002 -2.7755575615628914e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[33]" -type "matrix" "xform" 1 1 1 0 0 0 0 -0.93052999999999919
		 0.40000000000000002 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[34]" -type "matrix" "xform" 1 1 1 0 0 0 0 0.86637208112808017
		 2.2204460492503131e-16 4.4408920985006262e-16 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[35]" -type "matrix" "xform" 1 1 1 0 0 0 0 -0.86636999999999986
		 1.9428902930940239e-15 3.2782812020570873e-09 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[36]" -type "matrix" "xform" 1 1 1 0 0 0 0 1.7042113670357075
		 0 -3.9443045261050608e-31 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[37]" -type "matrix" "xform" 1 1 1 0 0 0 0 0.93052999999999919
		 -0.40000000000000002 -2.7755575615628914e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[38]" -type "matrix" "xform" 1 1 1 0 0 0 0 -0.93052999999999919
		 0.40000000000000002 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[39]" -type "matrix" "xform" 1 1 1 0 0 0 0 0.86637208112808017
		 2.2204460492503131e-16 4.4408920985006262e-16 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[40]" -type "matrix" "xform" 1 1 1 0 0 0 0 -0.86636999999999986
		 1.9428902930940239e-15 3.2782812020570873e-09 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[41]" -type "matrix" "xform" 1 1 1 0 0 0 0 0.93052999999999997
		 -0.4000000000000003 -5.5511151231257827e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[42]" -type "matrix" "xform" 1 1 1 0 0 0 0 -0.93052999999999997
		 0.4000000000000003 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[43]" -type "matrix" "xform" 1 1 1 0 0 0 0 0.86637208112808017
		 2.4980018054066022e-16 6.6613381477509392e-16 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[44]" -type "matrix" "xform" 1 1 1 0 0 0 0 -0.86636999999999986
		 1.915134717478395e-15 3.2782816461462971e-09 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[46]" -type "matrix" "xform" 1 1 1 -1.5707963267948963 -1.5707963267948963 0 0 0.15550527152436899
		 1.6140934910644489 6.0748788119920695e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr -s 31 ".m";
	setAttr -s 31 ".p";
	setAttr -s 5 ".g";
	setAttr ".g[4]" yes;
	setAttr ".g[9]" yes;
	setAttr ".g[22]" yes;
	setAttr ".g[28]" yes;
	setAttr ".g[46]" yes;
	setAttr ".bp" yes;
createNode polyMapDel -n "polyMapDel1";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002434";
	setAttr ".uopa" yes;
	setAttr ".ics" -type "componentList" 1 "f[*]";
createNode polyMapDel -n "polyMapDel3";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002435";
	setAttr ".uopa" yes;
	setAttr ".ics" -type "componentList" 1 "f[*]";
createNode skinCluster -n "skinCluster1";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002436";
	setAttr -s 177 ".wl";
	setAttr -s 3 ".wl[0].w[14:16]"  0.42682248925418542 0.51534873247146606 0.057828778274348437;
	setAttr -s 3 ".wl[1].w[13:15]"  0.053599647195439887 0.74739809624674747 0.19900225655781245;
	setAttr -s 2 ".wl[2].w[13:14]"  0.33631282779974375 0.6636871722002563;
	setAttr -s 2 ".wl[3].w[13:14]"  0.98442657139404244 0.015573428605957619;
	setAttr -s 2 ".wl[4].w[12:13]"  0.26218921488075159 0.73781078511924847;
	setAttr -s 4 ".wl[5].w";
	setAttr ".wl[5].w[0]" 0.59499447656087912;
	setAttr ".wl[5].w[1]" 0.18000690137328745;
	setAttr ".wl[5].w[6]" 0.03258028247803927;
	setAttr ".wl[5].w[11]" 0.19241833958779417;
	setAttr -s 4 ".wl[6].w";
	setAttr ".wl[6].w[0]" 0.63964916399946181;
	setAttr ".wl[6].w[1]" 0.21477889114655108;
	setAttr ".wl[6].w[6]" 0.039654836253311905;
	setAttr ".wl[6].w[11]" 0.10591710860067524;
	setAttr -s 2 ".wl[7].w[13:14]"  0.29156810000281108 0.70843189999718892;
	setAttr -s 5 ".wl[8].w";
	setAttr ".wl[8].w[13]" 0.00016326631937179335;
	setAttr ".wl[8].w[14]" 0.99932156697476948;
	setAttr ".wl[8].w[15]" 0.00018373628716537486;
	setAttr ".wl[8].w[18]" 0.00015714612814062614;
	setAttr ".wl[8].w[24]" 0.00017428429055267808;
	setAttr -s 5 ".wl[9].w";
	setAttr ".wl[9].w[0]" 0.23132507503032684;
	setAttr ".wl[9].w[1]" 0.087315030465306573;
	setAttr ".wl[9].w[6]" 0.087314947531465861;
	setAttr ".wl[9].w[11]" 0.59027654237034499;
	setAttr ".wl[9].w[12]" 0.0037684046025558359;
	setAttr -s 4 ".wl[10].w";
	setAttr ".wl[10].w[0]" 0.30700848667961278;
	setAttr ".wl[10].w[1]" 0.18784330219194409;
	setAttr ".wl[10].w[6]" 0.18784311959180008;
	setAttr ".wl[10].w[11]" 0.31730509153664316;
	setAttr -s 5 ".wl[11].w";
	setAttr ".wl[11].w[14]" 0.1496484043446149;
	setAttr ".wl[11].w[15]" 0.22594891058905373;
	setAttr ".wl[11].w[16]" 0.089513742579574979;
	setAttr ".wl[11].w[18]" 0.53383088111877441;
	setAttr ".wl[11].w[19]" 0.0010580613679819638;
	setAttr -s 2 ".wl[12].w[18:19]"  0.022672877901156251 0.97732712209884387;
	setAttr -s 3 ".wl[13].w";
	setAttr ".wl[13].w[14]" 0.37790589401805974;
	setAttr ".wl[13].w[15]" 0.16378728678142454;
	setAttr ".wl[13].w[18]" 0.45830681920051575;
	setAttr -s 4 ".wl[14].w";
	setAttr ".wl[14].w[14]" 0.4352346866630078;
	setAttr ".wl[14].w[15]" 0.44341754913330078;
	setAttr ".wl[14].w[16]" 0.067842826886431257;
	setAttr ".wl[14].w[18]" 0.053504937317260165;
	setAttr -s 5 ".wl[15].w";
	setAttr ".wl[15].w[13]" 0.046589992770339199;
	setAttr ".wl[15].w[14]" 0.13214627545325239;
	setAttr ".wl[15].w[15]" 0.14918422698974609;
	setAttr ".wl[15].w[18]" 0.59123479030130344;
	setAttr ".wl[15].w[19]" 0.080844714485358946;
	setAttr -s 3 ".wl[16].w";
	setAttr ".wl[16].w[13]" 0.42525926502755718;
	setAttr ".wl[16].w[14]" 0.57263300845264908;
	setAttr ".wl[16].w[18]" 0.0021077265197936117;
	setAttr -s 2 ".wl[17].w";
	setAttr ".wl[17].w[14]" 0.7029152512550354;
	setAttr ".wl[17].w[18]" 0.2970847487449646;
	setAttr -s 5 ".wl[18].w";
	setAttr ".wl[18].w[13]" 0.00013605844252593798;
	setAttr ".wl[18].w[14]" 0.99937714733981076;
	setAttr ".wl[18].w[15]" 0.00018477913290310301;
	setAttr ".wl[18].w[18]" 0.0001592728141275838;
	setAttr ".wl[18].w[24]" 0.00014274227063262502;
	setAttr -s 3 ".wl[19].w";
	setAttr ".wl[19].w[13]" 0.78355644366054433;
	setAttr ".wl[19].w[14]" 0.18399775373076271;
	setAttr ".wl[19].w[18]" 0.032445802608692995;
	setAttr -s 4 ".wl[20].w";
	setAttr ".wl[20].w[13]" 0.69894975436789009;
	setAttr ".wl[20].w[14]" 0.038188225308245581;
	setAttr ".wl[20].w[18]" 0.12971165079980018;
	setAttr ".wl[20].w[19]" 0.13315036952406403;
	setAttr -s 2 ".wl[21].w[12:13]"  0.1744516836387332 0.82554831636126691;
	setAttr -s 3 ".wl[22].w";
	setAttr ".wl[22].w[13]" 0.052260969873492658;
	setAttr ".wl[22].w[18]" 0.54524965122730817;
	setAttr ".wl[22].w[19]" 0.40248937889919922;
	setAttr -s 3 ".wl[23].w";
	setAttr ".wl[23].w[13]" 0.84127012204057627;
	setAttr ".wl[23].w[14]" 0.026332350481493631;
	setAttr ".wl[23].w[18]" 0.13239752747792988;
	setAttr -s 2 ".wl[24].w[12:13]"  0.20507287139840269 0.79492712860159731;
	setAttr -s 3 ".wl[25].w";
	setAttr ".wl[25].w[13]" 0.23019942621114783;
	setAttr ".wl[25].w[14]" 0.41659379025575582;
	setAttr ".wl[25].w[18]" 0.35320678353309631;
	setAttr -s 2 ".wl[26].w[12:13]"  0.19739843225992951 0.80260156774007052;
	setAttr -s 2 ".wl[27].w[18:19]"  0.957861692694713 0.042138307305287011;
	setAttr -s 3 ".wl[28].w";
	setAttr ".wl[28].w[0]" 0.29014219575691752;
	setAttr ".wl[28].w[1]" 0.27522182144293295;
	setAttr ".wl[28].w[11]" 0.43463598280014942;
	setAttr -s 3 ".wl[29].w";
	setAttr ".wl[29].w[0]" 0.38951898309188249;
	setAttr ".wl[29].w[1]" 0.54133695965479711;
	setAttr ".wl[29].w[11]" 0.069144057253320429;
	setAttr -s 3 ".wl[30].w";
	setAttr ".wl[30].w[0]" 0.37914311001874856;
	setAttr ".wl[30].w[1]" 0.537470571783627;
	setAttr ".wl[30].w[11]" 0.083386318197624404;
	setAttr -s 3 ".wl[31].w";
	setAttr ".wl[31].w[0]" 0.41076496406215296;
	setAttr ".wl[31].w[1]" 0.51942111454676543;
	setAttr ".wl[31].w[11]" 0.069813921391081543;
	setAttr -s 3 ".wl[32].w";
	setAttr ".wl[32].w[0]" 0.4545897335171134;
	setAttr ".wl[32].w[1]" 0.46240199984149377;
	setAttr ".wl[32].w[11]" 0.083008266641392769;
	setAttr -s 3 ".wl[33].w";
	setAttr ".wl[33].w[0]" 0.36303746544769711;
	setAttr ".wl[33].w[1]" 0.51449201598839001;
	setAttr ".wl[33].w[11]" 0.12247051856391283;
	setAttr -s 3 ".wl[34].w";
	setAttr ".wl[34].w[0]" 0.21331087275815536;
	setAttr ".wl[34].w[1]" 0.76481666325233566;
	setAttr ".wl[34].w[11]" 0.021872463989508897;
	setAttr -s 3 ".wl[35].w";
	setAttr ".wl[35].w[0]" 0.28808465581789056;
	setAttr ".wl[35].w[1]" 0.69478059000042736;
	setAttr ".wl[35].w[11]" 0.017134754181682057;
	setAttr -s 3 ".wl[36].w";
	setAttr ".wl[36].w[0]" 0.40406930091476151;
	setAttr ".wl[36].w[1]" 0.58652714075713486;
	setAttr ".wl[36].w[11]" 0.0094035583281037345;
	setAttr -s 3 ".wl[37].w";
	setAttr ".wl[37].w[0]" 0.45304068023649058;
	setAttr ".wl[37].w[1]" 0.50908522525740396;
	setAttr ".wl[37].w[11]" 0.037874094506105502;
	setAttr ".wl[38].w[19]"  1;
	setAttr -s 2 ".wl[39].w[18:19]"  0.00044021967378390296 0.99955978032621617;
	setAttr -s 2 ".wl[40].w";
	setAttr ".wl[40].w[13]" 0.2532424191961426;
	setAttr ".wl[40].w[19]" 0.74675758080385723;
	setAttr -s 3 ".wl[41].w";
	setAttr ".wl[41].w[13]" 0.47679007505313337;
	setAttr ".wl[41].w[14]" 0.00064032817944111899;
	setAttr ".wl[41].w[19]" 0.52256959676742554;
	setAttr -s 3 ".wl[42].w";
	setAttr ".wl[42].w[13]" 0.39238116409760027;
	setAttr ".wl[42].w[18]" 0.00036533285005377027;
	setAttr ".wl[42].w[19]" 0.60725350305234604;
	setAttr ".wl[43].w[19]"  1;
	setAttr -s 3 ".wl[44].w";
	setAttr ".wl[44].w[13]" 0.46942499009416649;
	setAttr ".wl[44].w[14]" 0.0096342292661850456;
	setAttr ".wl[44].w[19]" 0.52094078063964844;
	setAttr -s 3 ".wl[45].w";
	setAttr ".wl[45].w[13]" 0.18498286591766455;
	setAttr ".wl[45].w[18]" 0.014960378539580314;
	setAttr ".wl[45].w[19]" 0.80005675554275524;
	setAttr -s 4 ".wl[46].w";
	setAttr ".wl[46].w[14]" 0.1702640932397968;
	setAttr ".wl[46].w[15]" 0.29670318961143494;
	setAttr ".wl[46].w[16]" 0.11147597037313048;
	setAttr ".wl[46].w[18]" 0.4215567467756377;
	setAttr -s 3 ".wl[47].w";
	setAttr ".wl[47].w[0]" 0.2037460654973984;
	setAttr ".wl[47].w[11]" 0.1750073043313492;
	setAttr ".wl[47].w[12]" 0.62124663017125237;
	setAttr -s 3 ".wl[48].w";
	setAttr ".wl[48].w[0]" 0.14202533662319183;
	setAttr ".wl[48].w[11]" 0.1313507447276151;
	setAttr ".wl[48].w[12]" 0.72662391864919307;
	setAttr -s 3 ".wl[49].w";
	setAttr ".wl[49].w[0]" 0.1370919942855835;
	setAttr ".wl[49].w[11]" 0.025560665302030827;
	setAttr ".wl[49].w[12]" 0.83734734041238557;
	setAttr -s 3 ".wl[50].w";
	setAttr ".wl[50].w[0]" 0.16014185547828674;
	setAttr ".wl[50].w[12]" 0.8327818908400666;
	setAttr ".wl[50].w[13]" 0.0070762536816468052;
	setAttr -s 3 ".wl[51].w";
	setAttr ".wl[51].w[0]" 0.15185685455799103;
	setAttr ".wl[51].w[12]" 0.80683636919417701;
	setAttr ".wl[51].w[13]" 0.041306776247831911;
	setAttr -s 3 ".wl[52].w";
	setAttr ".wl[52].w[0]" 0.13035468757152557;
	setAttr ".wl[52].w[12]" 0.80443706945222881;
	setAttr ".wl[52].w[13]" 0.065208242976245556;
	setAttr -s 3 ".wl[53].w";
	setAttr ".wl[53].w[0]" 0.10284927487373352;
	setAttr ".wl[53].w[12]" 0.83101833188189167;
	setAttr ".wl[53].w[13]" 0.06613239324437481;
	setAttr -s 4 ".wl[54].w";
	setAttr ".wl[54].w[13]" 0.1836258542456384;
	setAttr ".wl[54].w[14]" 0.18528043783137543;
	setAttr ".wl[54].w[18]" 0.43606447976802992;
	setAttr ".wl[54].w[19]" 0.19502922815495621;
	setAttr -s 2 ".wl[55].w[18:19]"  0.62617833779036924 0.37382166220963081;
	setAttr -s 2 ".wl[56].w[18:19]"  0.78753407987043333 0.21246592012956669;
	setAttr ".wl[57].w[19]"  1;
	setAttr ".wl[58].w[19]"  1;
	setAttr ".wl[59].w[19]"  1;
	setAttr ".wl[60].w[19]"  0.99999999999999989;
	setAttr ".wl[61].w[19]"  1;
	setAttr ".wl[62].w[19]"  1;
	setAttr ".wl[63].w[19]"  1;
	setAttr ".wl[64].w[19]"  0.99999999999999989;
	setAttr ".wl[65].w[19]"  1;
	setAttr -s 3 ".wl[66].w";
	setAttr ".wl[66].w[14]" 0.59536925473566971;
	setAttr ".wl[66].w[15]" 0.065823562443256378;
	setAttr ".wl[66].w[18]" 0.33880718282107392;
	setAttr -s 4 ".wl[67].w";
	setAttr ".wl[67].w[14]" 0.42050277319908225;
	setAttr ".wl[67].w[15]" 0.28009918332099915;
	setAttr ".wl[67].w[16]" 0.050633933985003599;
	setAttr ".wl[67].w[18]" 0.24876410949491504;
	setAttr -s 4 ".wl[68].w";
	setAttr ".wl[68].w[14]" 0.24741253273770961;
	setAttr ".wl[68].w[15]" 0.51850372286197577;
	setAttr ".wl[68].w[16]" 0.15067426927996608;
	setAttr ".wl[68].w[18]" 0.08340947512034852;
	setAttr -s 4 ".wl[69].w";
	setAttr ".wl[69].w[14]" 0.27626384083866035;
	setAttr ".wl[69].w[15]" 0.51549834012985229;
	setAttr ".wl[69].w[16]" 0.20551913329493121;
	setAttr ".wl[69].w[18]" 0.0027186857365561856;
	setAttr -s 3 ".wl[70].w[14:16]"  0.24761250134518839 0.6269296407699585 0.12545785788485309;
	setAttr -s 3 ".wl[71].w[14:16]"  0.099014774372618949 0.85241199880265373 0.048573226824727325;
	setAttr ".wl[72].w[19]"  1;
	setAttr ".wl[73].w[19]"  1;
	setAttr ".wl[74].w[19]"  1;
	setAttr ".wl[75].w[19]"  1;
	setAttr ".wl[76].w[19]"  1;
	setAttr -s 2 ".wl[77].w";
	setAttr ".wl[77].w[13]" 0.00018149219136558582;
	setAttr ".wl[77].w[19]" 0.99981850780863435;
	setAttr -s 2 ".wl[78].w";
	setAttr ".wl[78].w[13]" 0.00021285833552235706;
	setAttr ".wl[78].w[19]" 0.99978714166447757;
	setAttr -s 2 ".wl[79].w";
	setAttr ".wl[79].w[13]" 0.00013547583579737827;
	setAttr ".wl[79].w[19]" 0.99986452416420257;
	setAttr -s 2 ".wl[80].w";
	setAttr ".wl[80].w[13]" 1.282185550210304e-06;
	setAttr ".wl[80].w[19]" 0.99999871781444971;
	setAttr -s 4 ".wl[81].w";
	setAttr ".wl[81].w[13]" 0.59247395698554639;
	setAttr ".wl[81].w[14]" 0.09777321202294674;
	setAttr ".wl[81].w[18]" 0.037862160930395405;
	setAttr ".wl[81].w[19]" 0.27189067006111145;
	setAttr -s 4 ".wl[82].w";
	setAttr ".wl[82].w[12]" 0.031927291381459597;
	setAttr ".wl[82].w[13]" 0.81479911032934205;
	setAttr ".wl[82].w[14]" 6.3062643713455342e-05;
	setAttr ".wl[82].w[19]" 0.15321053564548492;
	setAttr -s 3 ".wl[83].w";
	setAttr ".wl[83].w[12]" 0.0030266555643340674;
	setAttr ".wl[83].w[13]" 0.806957298269246;
	setAttr ".wl[83].w[19]" 0.19001604616642001;
	setAttr -s 4 ".wl[84].w";
	setAttr ".wl[84].w[13]" 0.48814523085146144;
	setAttr ".wl[84].w[14]" 0.024321362453544319;
	setAttr ".wl[84].w[18]" 0.051441336649859962;
	setAttr ".wl[84].w[19]" 0.43609207004513439;
	setAttr -s 2 ".wl[85].w[18:19]"  0.29449158906936646 0.70550841093063354;
	setAttr -s 2 ".wl[86].w[18:19]"  0.37377637624740601 0.62622362375259399;
	setAttr -s 2 ".wl[87].w[18:19]"  0.33660048246383667 0.66339951753616333;
	setAttr -s 2 ".wl[88].w[18:19]"  0.33234024047851562 0.66765975952148438;
	setAttr -s 4 ".wl[89].w";
	setAttr ".wl[89].w[13]" 0.3040494707684292;
	setAttr ".wl[89].w[14]" 0.037521160146159464;
	setAttr ".wl[89].w[18]" 0.15290711795626094;
	setAttr ".wl[89].w[19]" 0.50552225112915039;
	setAttr -s 4 ".wl[90].w";
	setAttr ".wl[90].w[14]" 0.3031977241215783;
	setAttr ".wl[90].w[15]" 0.29652422087968777;
	setAttr ".wl[90].w[16]" 0.037300361345418143;
	setAttr ".wl[90].w[18]" 0.36297769365331578;
	setAttr -s 4 ".wl[91].w";
	setAttr ".wl[91].w[14]" 0.23470927070027087;
	setAttr ".wl[91].w[15]" 0.45633038923993213;
	setAttr ".wl[91].w[16]" 0.14987203481406519;
	setAttr ".wl[91].w[18]" 0.1590883052457317;
	setAttr -s 2 ".wl[92].w";
	setAttr ".wl[92].w[14]" 0.42544721088622367;
	setAttr ".wl[92].w[18]" 0.57455278911377639;
	setAttr ".wl[93].w[14]"  1;
	setAttr -s 4 ".wl[94].w";
	setAttr ".wl[94].w[14]" 0.25590326465699026;
	setAttr ".wl[94].w[15]" 0.60685759201680411;
	setAttr ".wl[94].w[16]" 0.11008149665403004;
	setAttr ".wl[94].w[18]" 0.027157646672175576;
	setAttr -s 4 ".wl[95].w";
	setAttr ".wl[95].w[14]" 0.23903265337068316;
	setAttr ".wl[95].w[15]" 0.67854733158763336;
	setAttr ".wl[95].w[16]" 0.081866818009824829;
	setAttr ".wl[95].w[18]" 0.0005531970318587053;
	setAttr -s 3 ".wl[96].w[14:16]"  0.16647575198954756 0.792153976330781 0.041370271679671437;
	setAttr -s 5 ".wl[97].w";
	setAttr ".wl[97].w[14]" 0.18093131472126189;
	setAttr ".wl[97].w[15]" 0.27318229233847008;
	setAttr ".wl[97].w[16]" 0.1082258600342694;
	setAttr ".wl[97].w[24]" 0.43638128042221069;
	setAttr ".wl[97].w[25]" 0.0012792524837880685;
	setAttr -s 2 ".wl[98].w[24:25]"  0.022672915696730293 0.97732708430326964;
	setAttr -s 3 ".wl[99].w";
	setAttr ".wl[99].w[14]" 0.37250499501436302;
	setAttr ".wl[99].w[15]" 0.16144649610311432;
	setAttr ".wl[99].w[24]" 0.46604850888252258;
	setAttr -s 4 ".wl[100].w";
	setAttr ".wl[100].w[14]" 0.33490376756711432;
	setAttr ".wl[100].w[15]" 0.39421363454060299;
	setAttr ".wl[100].w[16]" 0.052203601925371275;
	setAttr ".wl[100].w[24]" 0.21867899596691132;
	setAttr -s 5 ".wl[101].w";
	setAttr ".wl[101].w[13]" 0.066471815687915728;
	setAttr ".wl[101].w[14]" 0.18853729987147505;
	setAttr ".wl[101].w[15]" 0.17151364684104919;
	setAttr ".wl[101].w[24]" 0.45813319453970303;
	setAttr ".wl[101].w[25]" 0.11534404305985706;
	setAttr -s 3 ".wl[102].w";
	setAttr ".wl[102].w[13]" 0.42525926502755729;
	setAttr ".wl[102].w[14]" 0.57263300845264919;
	setAttr ".wl[102].w[24]" 0.0021077265197936117;
	setAttr -s 2 ".wl[103].w";
	setAttr ".wl[103].w[14]" 0.76347808539867412;
	setAttr ".wl[103].w[24]" 0.23652191460132599;
	setAttr -s 3 ".wl[104].w";
	setAttr ".wl[104].w[13]" 0.7835558422793667;
	setAttr ".wl[104].w[14]" 0.18399805155582988;
	setAttr ".wl[104].w[24]" 0.032446106164803402;
	setAttr -s 4 ".wl[105].w";
	setAttr ".wl[105].w[13]" 0.69894975436789009;
	setAttr ".wl[105].w[14]" 0.038188225308245581;
	setAttr ".wl[105].w[24]" 0.12971165079980018;
	setAttr ".wl[105].w[25]" 0.13315036952406403;
	setAttr -s 2 ".wl[106].w[12:13]"  0.17445070267602997 0.82554929732397009;
	setAttr -s 3 ".wl[107].w";
	setAttr ".wl[107].w[13]" 0.066101092777776496;
	setAttr ".wl[107].w[24]" 0.68964622549004573;
	setAttr ".wl[107].w[25]" 0.24425268173217771;
	setAttr -s 3 ".wl[108].w";
	setAttr ".wl[108].w[13]" 0.84127012204057627;
	setAttr ".wl[108].w[14]" 0.026332350481493631;
	setAttr ".wl[108].w[24]" 0.13239752747792988;
	setAttr -s 2 ".wl[109].w[12:13]"  0.20507287061722743 0.79492712938277243;
	setAttr -s 3 ".wl[110].w";
	setAttr ".wl[110].w[13]" 0.22964650313032112;
	setAttr ".wl[110].w[14]" 0.41559821446764034;
	setAttr ".wl[110].w[24]" 0.35475528240203857;
	setAttr -s 2 ".wl[111].w[12:13]"  0.19739843656962927 0.8026015634303707;
	setAttr -s 2 ".wl[112].w[24:25]"  0.95786169450742042 0.042138305492579464;
	setAttr -s 3 ".wl[113].w";
	setAttr ".wl[113].w[0]" 0.26677218079566956;
	setAttr ".wl[113].w[6]" 0.28428273507780999;
	setAttr ".wl[113].w[11]" 0.44894508412652046;
	setAttr -s 3 ".wl[114].w";
	setAttr ".wl[114].w[0]" 0.38951898309188249;
	setAttr ".wl[114].w[6]" 0.54133695965479711;
	setAttr ".wl[114].w[11]" 0.069144057253320429;
	setAttr -s 3 ".wl[115].w";
	setAttr ".wl[115].w[0]" 0.37914310965739106;
	setAttr ".wl[115].w[6]" 0.53747057609276172;
	setAttr ".wl[115].w[11]" 0.083386314249847202;
	setAttr -s 3 ".wl[116].w";
	setAttr ".wl[116].w[0]" 0.41076496076397506;
	setAttr ".wl[116].w[6]" 0.51942112529330842;
	setAttr ".wl[116].w[11]" 0.069813913942716549;
	setAttr -s 3 ".wl[117].w";
	setAttr ".wl[117].w[0]" 0.45458973269343544;
	setAttr ".wl[117].w[6]" 0.46240199362437223;
	setAttr ".wl[117].w[11]" 0.083008273682192268;
	setAttr -s 3 ".wl[118].w";
	setAttr ".wl[118].w[0]" 0.3630374609511538;
	setAttr ".wl[118].w[6]" 0.51449202446253817;
	setAttr ".wl[118].w[11]" 0.122470514586308;
	setAttr -s 3 ".wl[119].w";
	setAttr ".wl[119].w[0]" 0.21331086968832536;
	setAttr ".wl[119].w[6]" 0.76481666559964012;
	setAttr ".wl[119].w[11]" 0.02187246471203444;
	setAttr -s 3 ".wl[120].w";
	setAttr ".wl[120].w[0]" 0.28808465581789061;
	setAttr ".wl[120].w[6]" 0.69478059000042747;
	setAttr ".wl[120].w[11]" 0.017134754181682057;
	setAttr -s 3 ".wl[121].w";
	setAttr ".wl[121].w[0]" 0.4040693002229741;
	setAttr ".wl[121].w[6]" 0.5865271414394958;
	setAttr ".wl[121].w[11]" 0.009403558337530038;
	setAttr -s 3 ".wl[122].w";
	setAttr ".wl[122].w[0]" 0.45304068023649058;
	setAttr ".wl[122].w[6]" 0.50908522525740396;
	setAttr ".wl[122].w[11]" 0.037874094506105502;
	setAttr ".wl[123].w[25]"  1;
	setAttr -s 2 ".wl[124].w[24:25]"  0.00044021969320646667 0.99955978030679349;
	setAttr -s 2 ".wl[125].w";
	setAttr ".wl[125].w[13]" 0.25324240581118185;
	setAttr ".wl[125].w[25]" 0.74675759418881804;
	setAttr -s 3 ".wl[126].w";
	setAttr ".wl[126].w[13]" 0.48499281991984666;
	setAttr ".wl[126].w[14]" 0.00065134178135579153;
	setAttr ".wl[126].w[25]" 0.51435583829879761;
	setAttr -s 3 ".wl[127].w";
	setAttr ".wl[127].w[13]" 0.39238116409760027;
	setAttr ".wl[127].w[24]" 0.00036533285005377027;
	setAttr ".wl[127].w[25]" 0.60725350305234604;
	setAttr ".wl[128].w[25]"  1;
	setAttr -s 3 ".wl[129].w";
	setAttr ".wl[129].w[13]" 0.46046919662845809;
	setAttr ".wl[129].w[14]" 0.0094504253159694226;
	setAttr ".wl[129].w[25]" 0.53008037805557251;
	setAttr -s 3 ".wl[130].w";
	setAttr ".wl[130].w[13]" 0.15378638597552544;
	setAttr ".wl[130].w[24]" 0.012437381900288556;
	setAttr ".wl[130].w[25]" 0.83377623212418606;
	setAttr -s 4 ".wl[131].w";
	setAttr ".wl[131].w[14]" 0.1842271968048374;
	setAttr ".wl[131].w[15]" 0.28196425200779496;
	setAttr ".wl[131].w[16]" 0.1206179479311421;
	setAttr ".wl[131].w[24]" 0.41319060325622559;
	setAttr -s 3 ".wl[132].w";
	setAttr ".wl[132].w[0]" 0.16819888353347778;
	setAttr ".wl[132].w[11]" 0.12734372708355296;
	setAttr ".wl[132].w[12]" 0.7044573893829692;
	setAttr -s 3 ".wl[133].w";
	setAttr ".wl[133].w[0]" 0.11676718294620514;
	setAttr ".wl[133].w[11]" 0.026162717544601751;
	setAttr ".wl[133].w[12]" 0.85707009950919311;
	setAttr -s 3 ".wl[134].w";
	setAttr ".wl[134].w[0]" 0.12397897243499756;
	setAttr ".wl[134].w[12]" 0.86864008226853573;
	setAttr ".wl[134].w[13]" 0.0073809452964667928;
	setAttr -s 3 ".wl[135].w";
	setAttr ".wl[135].w[0]" 0.12763652205467224;
	setAttr ".wl[135].w[12]" 0.8298771084722214;
	setAttr ".wl[135].w[13]" 0.042486369473106231;
	setAttr -s 3 ".wl[136].w";
	setAttr ".wl[136].w[0]" 0.12467905879020692;
	setAttr ".wl[136].w[12]" 0.80968713178057461;
	setAttr ".wl[136].w[13]" 0.06563380942921844;
	setAttr -s 4 ".wl[137].w";
	setAttr ".wl[137].w[13]" 0.23004511882846879;
	setAttr ".wl[137].w[14]" 0.23211953559272677;
	setAttr ".wl[137].w[24]" 0.29350060224533081;
	setAttr ".wl[137].w[25]" 0.2443347433334736;
	setAttr -s 2 ".wl[138].w[24:25]"  0.38066735863685608 0.61933264136314392;
	setAttr -s 2 ".wl[139].w[24:25]"  0.54680418968200684 0.45319581031799311;
	setAttr ".wl[140].w[25]"  1;
	setAttr ".wl[141].w[25]"  1;
	setAttr ".wl[142].w[25]"  1;
	setAttr ".wl[143].w[25]"  1;
	setAttr ".wl[144].w[25]"  0.99999999999999989;
	setAttr ".wl[145].w[25]"  1;
	setAttr ".wl[146].w[25]"  1;
	setAttr ".wl[147].w[25]"  1;
	setAttr ".wl[148].w[25]"  1;
	setAttr -s 3 ".wl[149].w";
	setAttr ".wl[149].w[14]" 0.65304577806546504;
	setAttr ".wl[149].w[15]" 0.070448517799377441;
	setAttr ".wl[149].w[24]" 0.27650570413515752;
	setAttr -s 4 ".wl[150].w";
	setAttr ".wl[150].w[14]" 0.45387643566946689;
	setAttr ".wl[150].w[15]" 0.2229619175195694;
	setAttr ".wl[150].w[16]" 0.054652165224075858;
	setAttr ".wl[150].w[24]" 0.26850948158688798;
	setAttr -s 4 ".wl[151].w";
	setAttr ".wl[151].w[14]" 0.23416125578533745;
	setAttr ".wl[151].w[15]" 0.41195842623710632;
	setAttr ".wl[151].w[16]" 0.14260430937474103;
	setAttr ".wl[151].w[24]" 0.2112760086028152;
	setAttr -s 4 ".wl[152].w";
	setAttr ".wl[152].w[14]" 0.16337555828520964;
	setAttr ".wl[152].w[15]" 0.58747765578963818;
	setAttr ".wl[152].w[16]" 0.12153963405919302;
	setAttr ".wl[152].w[24]" 0.12760715186595917;
	setAttr -s 3 ".wl[153].w[14:16]"  0.18285614135092057 0.72449613570910221 0.092647722939977195;
	setAttr ".wl[154].w[25]"  1;
	setAttr ".wl[155].w[25]"  1;
	setAttr ".wl[156].w[25]"  1;
	setAttr ".wl[157].w[25]"  1;
	setAttr ".wl[158].w[25]"  1;
	setAttr -s 2 ".wl[159].w";
	setAttr ".wl[159].w[13]" 0.00018149186078126109;
	setAttr ".wl[159].w[25]" 0.99981850813921858;
	setAttr -s 2 ".wl[160].w";
	setAttr ".wl[160].w[13]" 0.00021285493049420836;
	setAttr ".wl[160].w[25]" 0.99978714506950572;
	setAttr -s 2 ".wl[161].w";
	setAttr ".wl[161].w[13]" 0.00013547583579737827;
	setAttr ".wl[161].w[25]" 0.99986452416420257;
	setAttr -s 2 ".wl[162].w";
	setAttr ".wl[162].w[13]" 1.282105402550191e-06;
	setAttr ".wl[162].w[25]" 0.99999871789459749;
	setAttr -s 4 ".wl[163].w";
	setAttr ".wl[163].w[13]" 0.55829684799193136;
	setAttr ".wl[163].w[14]" 0.092133126080705813;
	setAttr ".wl[163].w[24]" 0.035678078657923114;
	setAttr ".wl[163].w[25]" 0.3138919472694397;
	setAttr -s 4 ".wl[164].w";
	setAttr ".wl[164].w[12]" 0.030606661764142083;
	setAttr ".wl[164].w[13]" 0.78108641180578275;
	setAttr ".wl[164].w[14]" 6.0452760069494278e-05;
	setAttr ".wl[164].w[25]" 0.1882464736700058;
	setAttr -s 3 ".wl[165].w";
	setAttr ".wl[165].w[12]" 0.0029985965565811211;
	setAttr ".wl[165].w[13]" 0.79947864400585789;
	setAttr ".wl[165].w[25]" 0.19752275943756104;
	setAttr -s 4 ".wl[166].w";
	setAttr ".wl[166].w[13]" 0.4881452332794689;
	setAttr ".wl[166].w[14]" 0.02432136601569523;
	setAttr ".wl[166].w[24]" 0.051441327350059088;
	setAttr ".wl[166].w[25]" 0.43609207335477679;
	setAttr -s 2 ".wl[167].w[24:25]"  0.35651451349258423 0.64348548650741577;
	setAttr -s 2 ".wl[168].w[24:25]"  0.31563258171081543 0.68436741828918457;
	setAttr -s 2 ".wl[169].w[24:25]"  0.27738261222839355 0.72261738777160645;
	setAttr -s 2 ".wl[170].w[24:25]"  0.26082020998001099 0.73917979001998901;
	setAttr -s 4 ".wl[171].w";
	setAttr ".wl[171].w[13]" 0.27100945140303395;
	setAttr ".wl[171].w[14]" 0.033443863597317949;
	setAttr ".wl[171].w[24]" 0.13629122276784472;
	setAttr ".wl[171].w[25]" 0.55925546223180334;
	setAttr -s 4 ".wl[172].w";
	setAttr ".wl[172].w[14]" 0.33015324164158572;
	setAttr ".wl[172].w[15]" 0.23398233950138092;
	setAttr ".wl[172].w[16]" 0.040616511941508435;
	setAttr ".wl[172].w[24]" 0.39524790691552497;
	setAttr -s 4 ".wl[173].w";
	setAttr ".wl[173].w[14]" 0.23470936453267313;
	setAttr ".wl[173].w[15]" 0.45633101329694353;
	setAttr ".wl[173].w[16]" 0.14987206844396211;
	setAttr ".wl[173].w[24]" 0.15908755372642125;
	setAttr -s 2 ".wl[174].w";
	setAttr ".wl[174].w[14]" 0.42544744569300591;
	setAttr ".wl[174].w[24]" 0.57455255430699403;
	setAttr -s 4 ".wl[175].w";
	setAttr ".wl[175].w[14]" 0.2559032646569902;
	setAttr ".wl[175].w[15]" 0.60685759201680411;
	setAttr ".wl[175].w[16]" 0.11008149665403;
	setAttr ".wl[175].w[24]" 0.027157646672175576;
	setAttr -s 4 ".wl[176].w";
	setAttr ".wl[176].w[14]" 0.23903265337068319;
	setAttr ".wl[176].w[15]" 0.67854733158763336;
	setAttr ".wl[176].w[16]" 0.081866818009824829;
	setAttr ".wl[176].w[24]" 0.0005531970318587053;
	setAttr -s 30 ".pm";
	setAttr ".pm[0]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -8.9231745720989668 0.17376929722515433 2.0199273074892598e-15 1;
	setAttr ".pm[1]" -type "matrix" -3.4450928483976665e-16 -2.2204460492503131e-16 -1 0 -1 4.9303806576313238e-32 3.4450928483976665e-16 0
		 -7.6496428045251064e-32 1 -2.2204460492503131e-16 0 8.9231745720989668 0.17376929722515455 0.999999999999997 1;
	setAttr ".pm[2]" -type "matrix" -3.4450928483976665e-16 -2.2204460492503131e-16 -1 0 -1 4.9303806576313238e-32 3.4450928483976665e-16 0
		 -7.6496428045251064e-32 1 -2.2204460492503131e-16 0 4.6515061293712359 0.17376929722515452 0.99999999999999889 1;
	setAttr ".pm[3]" -type "matrix" 5.8331365260285766e-07 -3.4717393473770988e-07 -0.99999999999976963 0 -0.4794097213532717 0.87759120270866275 -5.8432302659159539e-07 0
		 0.87759120270866331 0.47940972135350218 3.454723706304003e-07 0 0.53189973592848949 -0.61121325699033013 1.0000005224619188 1;
	setAttr ".pm[4]" -type "matrix" -3.7839275046629232e-09 -4.9514660478913824e-07 -0.99999999999987765 0 4.5717040610908244e-16 0.99999999999987776 -4.9514660478913814e-07 0
		 1.0000000000000002 -2.2981828101998501e-15 -3.7839275046623533e-09 0 -1.0271901970466448 -0.13533431203966553 1.0000008717993354 1;
	setAttr ".pm[5]" -type "matrix" -3.7839275046629232e-09 -4.9514660478913824e-07 -0.99999999999987765 0 4.5717040610908244e-16 0.99999999999987776 -4.9514660478913814e-07 0
		 1.0000000000000002 -2.2981828101998501e-15 -3.7839275046623533e-09 0 -1.8935622781747257 -0.1353343120396657 1.0000008717993347 1;
	setAttr ".pm[6]" -type "matrix" 2.2204460492503131e-16 9.9579925010295987e-17 -1 0 1 -2.2111185107375414e-32 2.2204460492503131e-16 0
		 4.9303806576313238e-32 -1 -9.9579925010295987e-17 0 -8.9231700000000007 -0.1737689999999999 -1.000000000000002 1;
	setAttr ".pm[7]" -type "matrix" 2.2204460492503131e-16 9.9579925010295987e-17 -1 0 1 -2.2111185107375414e-32 2.2204460492503131e-16 0
		 4.9303806576313238e-32 -1 -9.9579925010295987e-17 0 -4.65151 -0.1737689999999999 -1.0000000000000011 1;
	setAttr ".pm[8]" -type "matrix" 5.8331365260285766e-07 -3.4602377056398311e-07 -0.99999999999976996 0 0.47940972135327098 -0.87759120270866364 5.8331365263106153e-07 0
		 -0.87759120270866364 -0.47940972135350091 -3.460237705164382e-07 0 -0.53189953941047974 0.61121351838277305 -1.0000005217588994 1;
	setAttr ".pm[9]" -type "matrix" -3.7839275046628231e-09 -5.0889760207317231e-07 -0.99999999999987077 0 -5.094072503275622e-16 -0.99999999999987077 5.0889760207317231e-07 0
		 -1 2.5476401720380396e-15 3.7839275046620083e-09 0 1.0271899962160689 0.13533449110186921 -1.0000010727583399 1;
	setAttr ".pm[10]" -type "matrix" -3.7839275046628231e-09 -5.0889760207317231e-07 -0.99999999999987077 0 -5.094072503275622e-16 -0.99999999999987077 5.0889760207317231e-07 0
		 -1 2.5476401720380396e-15 3.7839275046620083e-09 0 1.8935599962160683 0.13533449110186729 -1.0000010760366214 1;
	setAttr ".pm[11]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -9.5109235153967138 0.17376929722515433 2.1504337893989135e-15 1;
	setAttr ".pm[12]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -10.500223672082353 0.17376929722515433 2.3701025518424469e-15 1;
	setAttr ".pm[13]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -11.703780240227058 0.17376929722515433 2.6373457945210649e-15 1;
	setAttr ".pm[14]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -12.875926312066481 0.17376929722515433 2.8976145059570766e-15 1;
	setAttr ".pm[15]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -13.928707643645982 0.17376929722515508 3.1313789208000969e-15 1;
	setAttr ".pm[16]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -15.338164390135388 0.17376929722515508 3.444341187233257e-15 1;
	setAttr ".pm[17]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -17.042375757171094 0.17376929722515508 3.4443411872332574e-15 1;
	setAttr ".pm[18]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -0.64419300000000002 -13.5276 0.17376900000000314 1;
	setAttr ".pm[19]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -1.6150599999999999 -13.512600000000001 0.17376900000000314 1;
	setAttr ".pm[20]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -4.4291700000000001 -13.512600000000001 0.17376900000000312 1;
	setAttr ".pm[21]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -6.9456699999999998 -13.512600000000001 0.17376900000000314 1;
	setAttr ".pm[22]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -7.7752400000000002 -13.512600000000001 0.17376900000000312 1;
	setAttr ".pm[23]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -8.7057699999999993 -13.1126 0.17376900000000317 1;
	setAttr ".pm[24]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 0.64419300000000002 13.5276 -0.17376900000000289 1;
	setAttr ".pm[25]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 1.6150599999999999 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[26]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 4.4291700000000001 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[27]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 6.9456699999999998 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[28]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 7.7752400000000002 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[29]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 8.7057699999999993 13.1126 -0.17376900000000289 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 0 0 0 1;
	setAttr -s 15 ".ma";
	setAttr -s 30 ".dpf[0:29]"  4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 
		4 4 4 4 4 4 4 4 4 4;
	setAttr -s 15 ".lw";
	setAttr ".mmi" yes;
	setAttr ".mi" 5;
	setAttr ".ucm" yes;
createNode tweak -n "tweak1";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002437";
createNode objectSet -n "skinCluster1Set";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002438";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster1GroupId";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002439";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster1GroupParts";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000243A";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode objectSet -n "tweakSet1";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000243B";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId2";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000243C";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts2";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000243D";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode skinCluster -n "skinCluster2";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000243E";
	setAttr -s 376 ".wl";
	setAttr -s 2 ".wl[0].w";
	setAttr ".wl[0].w[16]" 1;
	setAttr ".wl[0].w[26]" 0.18173997678770321;
	setAttr -s 2 ".wl[1].w";
	setAttr ".wl[1].w[16]" 1;
	setAttr ".wl[1].w[26]" 0.16996845786125792;
	setAttr -s 2 ".wl[2].w";
	setAttr ".wl[2].w[16]" 1;
	setAttr ".wl[2].w[26]" 0.17644768685459572;
	setAttr -s 2 ".wl[3].w";
	setAttr ".wl[3].w[16]" 1;
	setAttr ".wl[3].w[26]" 0.054058457577610269;
	setAttr -s 2 ".wl[4].w";
	setAttr ".wl[4].w[16]" 1;
	setAttr ".wl[4].w[26]" 0.057080215955173541;
	setAttr -s 2 ".wl[5].w";
	setAttr ".wl[5].w[16]" 1;
	setAttr ".wl[5].w[26]" 0.065596890716333303;
	setAttr -s 2 ".wl[6].w";
	setAttr ".wl[6].w[16]" 1;
	setAttr ".wl[6].w[26]" 0.067663379302971199;
	setAttr -s 2 ".wl[7].w";
	setAttr ".wl[7].w[16]" 1;
	setAttr ".wl[7].w[26]" 0.067475200779577665;
	setAttr -s 2 ".wl[8].w";
	setAttr ".wl[8].w[16]" 1;
	setAttr ".wl[8].w[26]" 0.064317350362392139;
	setAttr -s 2 ".wl[9].w";
	setAttr ".wl[9].w[16]" 1;
	setAttr ".wl[9].w[26]" 0.32512454069299496;
	setAttr -s 2 ".wl[10].w";
	setAttr ".wl[10].w[16]" 1;
	setAttr ".wl[10].w[26]" 0.53817530377648226;
	setAttr -s 2 ".wl[11].w";
	setAttr ".wl[11].w[16]" 1;
	setAttr ".wl[11].w[26]" 0.56354210397153626;
	setAttr -s 2 ".wl[12].w";
	setAttr ".wl[12].w[16]" 1;
	setAttr ".wl[12].w[26]" 0.31286691202533529;
	setAttr -s 2 ".wl[13].w";
	setAttr ".wl[13].w[16]" 1;
	setAttr ".wl[13].w[26]" 0.27264884660444327;
	setAttr -s 2 ".wl[14].w";
	setAttr ".wl[14].w[16]" 1;
	setAttr ".wl[14].w[26]" 0.14183794858824977;
	setAttr -s 2 ".wl[15].w";
	setAttr ".wl[15].w[16]" 1;
	setAttr ".wl[15].w[26]" 0.16014721386097547;
	setAttr -s 2 ".wl[16].w";
	setAttr ".wl[16].w[16]" 1;
	setAttr ".wl[16].w[26]" 0.42276426352630042;
	setAttr -s 2 ".wl[17].w";
	setAttr ".wl[17].w[16]" 1;
	setAttr ".wl[17].w[26]" 0.2645093185249846;
	setAttr -s 2 ".wl[18].w";
	setAttr ".wl[18].w[16]" 1;
	setAttr ".wl[18].w[26]" 0.12744577157337963;
	setAttr -s 2 ".wl[19].w";
	setAttr ".wl[19].w[16]" 1;
	setAttr ".wl[19].w[26]" 0.087457663692177834;
	setAttr -s 2 ".wl[20].w";
	setAttr ".wl[20].w[16]" 1;
	setAttr ".wl[20].w[26]" 0.093211885031429131;
	setAttr -s 2 ".wl[21].w";
	setAttr ".wl[21].w[16]" 1;
	setAttr ".wl[21].w[26]" 0.12399115592896176;
	setAttr -s 2 ".wl[22].w";
	setAttr ".wl[22].w[16]" 1;
	setAttr ".wl[22].w[26]" 0.20849312233012232;
	setAttr -s 2 ".wl[23].w";
	setAttr ".wl[23].w[16]" 1;
	setAttr ".wl[23].w[26]" 0.26844386606010462;
	setAttr -s 2 ".wl[24].w";
	setAttr ".wl[24].w[16]" 1;
	setAttr ".wl[24].w[26]" 0.076009850904089502;
	setAttr -s 2 ".wl[25].w";
	setAttr ".wl[25].w[16]" 1;
	setAttr ".wl[25].w[26]" 0.075929007451638234;
	setAttr -s 2 ".wl[26].w";
	setAttr ".wl[26].w[16]" 1;
	setAttr ".wl[26].w[26]" 0.096994354116435533;
	setAttr -s 2 ".wl[27].w";
	setAttr ".wl[27].w[16]" 1;
	setAttr ".wl[27].w[26]" 0.1411835445006859;
	setAttr -s 2 ".wl[28].w";
	setAttr ".wl[28].w[16]" 1;
	setAttr ".wl[28].w[26]" 0.05734330033120158;
	setAttr -s 2 ".wl[29].w";
	setAttr ".wl[29].w[16]" 1;
	setAttr ".wl[29].w[26]" 0.049014369707197795;
	setAttr ".wl[30].w[16]"  1;
	setAttr ".wl[31].w[16]"  1;
	setAttr ".wl[32].w[16]"  1;
	setAttr -s 2 ".wl[33].w";
	setAttr ".wl[33].w[16]" 1;
	setAttr ".wl[33].w[26]" 0.053415827733934343;
	setAttr -s 2 ".wl[34].w";
	setAttr ".wl[34].w[16]" 1;
	setAttr ".wl[34].w[26]" 0.04649832247234225;
	setAttr ".wl[35].w[16]"  1;
	setAttr ".wl[36].w[16]"  1;
	setAttr ".wl[37].w[16]"  1;
	setAttr ".wl[38].w[16]"  1;
	setAttr -s 2 ".wl[39].w";
	setAttr ".wl[39].w[16]" 1;
	setAttr ".wl[39].w[26]" 0.23029414872567527;
	setAttr -s 2 ".wl[40].w";
	setAttr ".wl[40].w[16]" 1;
	setAttr ".wl[40].w[26]" 0.22175205055439001;
	setAttr -s 2 ".wl[41].w";
	setAttr ".wl[41].w[16]" 1;
	setAttr ".wl[41].w[26]" 0.16995002410691268;
	setAttr -s 2 ".wl[42].w";
	setAttr ".wl[42].w[16]" 1;
	setAttr ".wl[42].w[26]" 0.16702319524850845;
	setAttr -s 2 ".wl[43].w";
	setAttr ".wl[43].w[16]" 1;
	setAttr ".wl[43].w[26]" 0.099946329715097884;
	setAttr -s 2 ".wl[44].w";
	setAttr ".wl[44].w[16]" 1;
	setAttr ".wl[44].w[26]" 0.13403434006702586;
	setAttr -s 2 ".wl[45].w";
	setAttr ".wl[45].w[16]" 1;
	setAttr ".wl[45].w[26]" 0.11507158443821676;
	setAttr -s 2 ".wl[46].w";
	setAttr ".wl[46].w[16]" 1;
	setAttr ".wl[46].w[26]" 0.09687497907874254;
	setAttr -s 2 ".wl[47].w";
	setAttr ".wl[47].w[16]" 1;
	setAttr ".wl[47].w[26]" 0.095340003809252116;
	setAttr -s 2 ".wl[48].w";
	setAttr ".wl[48].w[16]" 1;
	setAttr ".wl[48].w[26]" 0.088908816869568086;
	setAttr -s 2 ".wl[49].w";
	setAttr ".wl[49].w[16]" 1;
	setAttr ".wl[49].w[26]" 0.084211168894444244;
	setAttr -s 2 ".wl[50].w";
	setAttr ".wl[50].w[16]" 1;
	setAttr ".wl[50].w[26]" 0.069936627234088819;
	setAttr -s 2 ".wl[51].w";
	setAttr ".wl[51].w[16]" 1;
	setAttr ".wl[51].w[26]" 0.056635925990565751;
	setAttr -s 2 ".wl[52].w";
	setAttr ".wl[52].w[16]" 1;
	setAttr ".wl[52].w[26]" 0.053445512379637197;
	setAttr -s 2 ".wl[53].w";
	setAttr ".wl[53].w[16]" 1;
	setAttr ".wl[53].w[26]" 0.061109769556976286;
	setAttr ".wl[54].w[16]"  1;
	setAttr ".wl[55].w[16]"  1;
	setAttr ".wl[56].w[16]"  1;
	setAttr ".wl[57].w[16]"  1;
	setAttr -s 2 ".wl[58].w";
	setAttr ".wl[58].w[16]" 1;
	setAttr ".wl[58].w[26]" 0.032865045583631639;
	setAttr ".wl[59].w[16]"  0.99999999999999989;
	setAttr -s 3 ".wl[60].w[14:16]"  0.00018178614171665474 0.00025416223017055232 0.99956405162811279;
	setAttr ".wl[61].w[16]"  1;
	setAttr -s 2 ".wl[62].w";
	setAttr ".wl[62].w[16]" 1;
	setAttr ".wl[62].w[26]" 0.077226152337212695;
	setAttr -s 2 ".wl[63].w";
	setAttr ".wl[63].w[16]" 1;
	setAttr ".wl[63].w[26]" 0.22539871319016641;
	setAttr -s 2 ".wl[64].w";
	setAttr ".wl[64].w[16]" 1;
	setAttr ".wl[64].w[26]" 0.4250062206607762;
	setAttr -s 2 ".wl[65].w";
	setAttr ".wl[65].w[16]" 1;
	setAttr ".wl[65].w[26]" 0.58086445740599424;
	setAttr -s 2 ".wl[66].w";
	setAttr ".wl[66].w[16]" 1;
	setAttr ".wl[66].w[26]" 0.65326533510412454;
	setAttr -s 2 ".wl[67].w";
	setAttr ".wl[67].w[16]" 1;
	setAttr ".wl[67].w[26]" 0.079798952643402879;
	setAttr -s 2 ".wl[68].w";
	setAttr ".wl[68].w[16]" 1;
	setAttr ".wl[68].w[26]" 0.073190963802867035;
	setAttr -s 2 ".wl[69].w";
	setAttr ".wl[69].w[16]" 1;
	setAttr ".wl[69].w[26]" 0.063236448609249457;
	setAttr -s 2 ".wl[70].w";
	setAttr ".wl[70].w[16]" 1;
	setAttr ".wl[70].w[26]" 0.055264495718810654;
	setAttr -s 2 ".wl[71].w";
	setAttr ".wl[71].w[16]" 1;
	setAttr ".wl[71].w[26]" 0.054678102870320898;
	setAttr -s 2 ".wl[72].w";
	setAttr ".wl[72].w[16]" 1;
	setAttr ".wl[72].w[26]" 0.064442987001657043;
	setAttr ".wl[73].w[16]"  1;
	setAttr ".wl[74].w[16]"  1;
	setAttr -s 2 ".wl[75].w";
	setAttr ".wl[75].w[16]" 1;
	setAttr ".wl[75].w[26]" 0.066104020352172776;
	setAttr -s 2 ".wl[76].w";
	setAttr ".wl[76].w[16]" 1;
	setAttr ".wl[76].w[26]" 0.072003350354434642;
	setAttr -s 2 ".wl[77].w";
	setAttr ".wl[77].w[16]" 1;
	setAttr ".wl[77].w[26]" 0.11401218741381113;
	setAttr -s 2 ".wl[78].w";
	setAttr ".wl[78].w[16]" 1;
	setAttr ".wl[78].w[26]" 0.016007854781700994;
	setAttr -s 2 ".wl[79].w";
	setAttr ".wl[79].w[16]" 1;
	setAttr ".wl[79].w[26]" 0.016551651972583445;
	setAttr -s 2 ".wl[80].w";
	setAttr ".wl[80].w[16]" 1;
	setAttr ".wl[80].w[26]" 0.010041257873585428;
	setAttr -s 2 ".wl[81].w";
	setAttr ".wl[81].w[16]" 1;
	setAttr ".wl[81].w[26]" 0.0087982501753074427;
	setAttr ".wl[82].w[16]"  1;
	setAttr ".wl[83].w[16]"  1;
	setAttr ".wl[84].w[16]"  1;
	setAttr ".wl[85].w[16]"  1;
	setAttr -s 2 ".wl[86].w";
	setAttr ".wl[86].w[16]" 1;
	setAttr ".wl[86].w[26]" 0.029786096565286128;
	setAttr -s 2 ".wl[87].w";
	setAttr ".wl[87].w[16]" 1;
	setAttr ".wl[87].w[26]" 0.024822132968059189;
	setAttr -s 2 ".wl[88].w";
	setAttr ".wl[88].w[16]" 1;
	setAttr ".wl[88].w[26]" 0.055998814215146478;
	setAttr -s 2 ".wl[89].w";
	setAttr ".wl[89].w[16]" 1;
	setAttr ".wl[89].w[26]" 0.034936967881675558;
	setAttr -s 2 ".wl[90].w";
	setAttr ".wl[90].w[16]" 1;
	setAttr ".wl[90].w[26]" 0.08992113332976176;
	setAttr -s 2 ".wl[91].w";
	setAttr ".wl[91].w[16]" 1;
	setAttr ".wl[91].w[26]" 0.11394617207685429;
	setAttr -s 2 ".wl[92].w";
	setAttr ".wl[92].w[16]" 1;
	setAttr ".wl[92].w[26]" 0.14051634320026288;
	setAttr -s 2 ".wl[93].w";
	setAttr ".wl[93].w[16]" 1;
	setAttr ".wl[93].w[26]" 0.084280511640595454;
	setAttr -s 2 ".wl[94].w";
	setAttr ".wl[94].w[16]" 1;
	setAttr ".wl[94].w[26]" 0.52283208619067922;
	setAttr -s 2 ".wl[95].w";
	setAttr ".wl[95].w[16]" 1;
	setAttr ".wl[95].w[26]" 0.029630674713159527;
	setAttr -s 2 ".wl[96].w";
	setAttr ".wl[96].w[16]" 1;
	setAttr ".wl[96].w[26]" 0.013199134156415186;
	setAttr -s 2 ".wl[97].w";
	setAttr ".wl[97].w[16]" 1;
	setAttr ".wl[97].w[26]" 0.001739864177842986;
	setAttr -s 2 ".wl[98].w";
	setAttr ".wl[98].w[16]" 1;
	setAttr ".wl[98].w[26]" 0.012461169002131125;
	setAttr -s 2 ".wl[99].w";
	setAttr ".wl[99].w[16]" 1;
	setAttr ".wl[99].w[26]" 0.0057048804790057906;
	setAttr -s 2 ".wl[100].w";
	setAttr ".wl[100].w[16]" 1;
	setAttr ".wl[100].w[26]" 0.0015483661032310203;
	setAttr -s 2 ".wl[101].w";
	setAttr ".wl[101].w[16]" 1;
	setAttr ".wl[101].w[26]" 0.0080852827465468739;
	setAttr -s 2 ".wl[102].w";
	setAttr ".wl[102].w[16]" 1;
	setAttr ".wl[102].w[26]" 0.0086638569015507552;
	setAttr -s 2 ".wl[103].w";
	setAttr ".wl[103].w[16]" 1;
	setAttr ".wl[103].w[26]" 0.0074934646096409463;
	setAttr ".wl[104].w[16]"  1;
	setAttr ".wl[105].w[16]"  1;
	setAttr ".wl[106].w[16]"  1;
	setAttr ".wl[107].w[16]"  1;
	setAttr ".wl[108].w[16]"  1;
	setAttr ".wl[109].w[16]"  1;
	setAttr -s 2 ".wl[110].w";
	setAttr ".wl[110].w[16]" 1;
	setAttr ".wl[110].w[26]" 0.3316495462300042;
	setAttr -s 2 ".wl[111].w";
	setAttr ".wl[111].w[16]" 1;
	setAttr ".wl[111].w[26]" 0.16703979298311974;
	setAttr -s 2 ".wl[112].w";
	setAttr ".wl[112].w[16]" 1;
	setAttr ".wl[112].w[26]" 0.61936611219507143;
	setAttr -s 2 ".wl[113].w";
	setAttr ".wl[113].w[16]" 1;
	setAttr ".wl[113].w[26]" 0.13660533664625424;
	setAttr -s 4 ".wl[114].w";
	setAttr ".wl[114].w[14]" 2.0144110898146402e-05;
	setAttr ".wl[114].w[15]" 0.0002248897597405011;
	setAttr ".wl[114].w[16]" 0.99975496612936132;
	setAttr ".wl[114].w[26]" 0.00023251863896481807;
	setAttr -s 2 ".wl[115].w";
	setAttr ".wl[115].w[16]" 1;
	setAttr ".wl[115].w[26]" 0.00067369804469110924;
	setAttr -s 2 ".wl[116].w";
	setAttr ".wl[116].w[16]" 1;
	setAttr ".wl[116].w[26]" 0.0064771335898634102;
	setAttr ".wl[117].w[16]"  1;
	setAttr ".wl[118].w[16]"  1;
	setAttr -s 2 ".wl[119].w";
	setAttr ".wl[119].w[16]" 1;
	setAttr ".wl[119].w[26]" 0.021881121672221397;
	setAttr ".wl[120].w[16]"  1;
	setAttr ".wl[121].w[16]"  1;
	setAttr ".wl[122].w[16]"  1;
	setAttr -s 3 ".wl[123].w[14:16]"  0.2788966817049725 0.61028575486528358 0.110817563429744;
	setAttr -s 4 ".wl[124].w";
	setAttr ".wl[124].w[14]" 0.19001959150066203;
	setAttr ".wl[124].w[15]" 0.58978482420306388;
	setAttr ".wl[124].w[16]" 0.20840477992472209;
	setAttr ".wl[124].w[18]" 0.011790804371552048;
	setAttr -s 3 ".wl[125].w[14:16]"  0.060280940119984382 0.1509278636460038 0.78879119623401173;
	setAttr -s 3 ".wl[126].w[14:16]"  0.1198713756291616 0.3783932531641005 0.50173537120673795;
	setAttr -s 3 ".wl[127].w[14:16]"  0.15366323713246252 0.41295674755686768 0.43338001531066994;
	setAttr -s 3 ".wl[128].w[14:16]"  0.34682555498293022 0.59643520323534371 0.056739241781725992;
	setAttr -s 3 ".wl[129].w[14:16]"  0.054171956340126275 0.096376097077887399 0.84945194658198619;
	setAttr -s 4 ".wl[130].w";
	setAttr ".wl[130].w[14]" 0.31230561050497124;
	setAttr ".wl[130].w[15]" 0.2518920138931654;
	setAttr ".wl[130].w[16]" 0.071157637796035969;
	setAttr ".wl[130].w[18]" 0.3646447378058274;
	setAttr -s 4 ".wl[131].w";
	setAttr ".wl[131].w[14]" 0.11270222234820236;
	setAttr ".wl[131].w[15]" 0.13818736631485762;
	setAttr ".wl[131].w[16]" 0.0064148886754218284;
	setAttr ".wl[131].w[18]" 0.74269552266151828;
	setAttr -s 3 ".wl[132].w[14:16]"  0.054271075515066679 0.10676278983321975 0.83896613465171355;
	setAttr -s 3 ".wl[133].w[14:16]"  0.062492616838737795 0.21142967560686204 0.72607770755440015;
	setAttr -s 3 ".wl[134].w[14:16]"  0.035410419792360634 0.42816252516307873 0.53642705504456067;
	setAttr -s 3 ".wl[135].w[14:16]"  0.021126386642035078 0.5230432548966033 0.45583035846136166;
	setAttr -s 4 ".wl[136].w";
	setAttr ".wl[136].w[14]" 0.20622945607094403;
	setAttr ".wl[136].w[15]" 0.58541857140908271;
	setAttr ".wl[136].w[16]" 0.1909894738858986;
	setAttr ".wl[136].w[18]" 0.017362498634074516;
	setAttr -s 4 ".wl[137].w";
	setAttr ".wl[137].w[14]" 0.27810361500321346;
	setAttr ".wl[137].w[15]" 0.56295831697387211;
	setAttr ".wl[137].w[16]" 0.099442388458644337;
	setAttr ".wl[137].w[18]" 0.059495679564270085;
	setAttr -s 4 ".wl[138].w";
	setAttr ".wl[138].w[14]" 0.2351093765723424;
	setAttr ".wl[138].w[15]" 0.68361336679149221;
	setAttr ".wl[138].w[16]" 0.080815465705272038;
	setAttr ".wl[138].w[18]" 0.00046179093089342708;
	setAttr -s 3 ".wl[139].w[14:16]"  0.19918273166727937 0.74856348327079281 0.052253785061927897;
	setAttr -s 3 ".wl[140].w[14:16]"  0.46923672080320872 0.49879849036176449 0.031964788835026771;
	setAttr -s 2 ".wl[141].w[14:15]"  0.84637489390624587 0.15362510609375413;
	setAttr -s 4 ".wl[142].w";
	setAttr ".wl[142].w[14]" 0.50930645667522745;
	setAttr ".wl[142].w[15]" 0.30049569922966773;
	setAttr ".wl[142].w[16]" 0.0068520047138867649;
	setAttr ".wl[142].w[18]" 0.18334583938121796;
	setAttr -s 4 ".wl[143].w";
	setAttr ".wl[143].w[14]" 0.28409235725029447;
	setAttr ".wl[143].w[15]" 0.2452988834486845;
	setAttr ".wl[143].w[16]" 0.00068866051943543662;
	setAttr ".wl[143].w[18]" 0.46992009878158569;
	setAttr -s 4 ".wl[144].w";
	setAttr ".wl[144].w[14]" 0.20148467696553091;
	setAttr ".wl[144].w[15]" 0.25495133735453218;
	setAttr ".wl[144].w[16]" 0.1179646719403562;
	setAttr ".wl[144].w[18]" 0.42559931373958082;
	setAttr -s 4 ".wl[145].w";
	setAttr ".wl[145].w[14]" 0.16346131017049986;
	setAttr ".wl[145].w[15]" 0.22721994341556159;
	setAttr ".wl[145].w[16]" 0.11215224878371378;
	setAttr ".wl[145].w[18]" 0.4971664976302248;
	setAttr -s 4 ".wl[146].w";
	setAttr ".wl[146].w[14]" 0.13090216166500218;
	setAttr ".wl[146].w[15]" 0.20399526401040627;
	setAttr ".wl[146].w[16]" 0.084152752817790749;
	setAttr ".wl[146].w[18]" 0.58094982150680086;
	setAttr -s 2 ".wl[147].w";
	setAttr ".wl[147].w[14]" 0.69198346399347277;
	setAttr ".wl[147].w[18]" 0.30801653600652723;
	setAttr -s 2 ".wl[148].w";
	setAttr ".wl[148].w[14]" 0.3268972635269165;
	setAttr ".wl[148].w[18]" 0.6731027364730835;
	setAttr ".wl[149].w[14]"  1;
	setAttr -s 5 ".wl[150].w";
	setAttr ".wl[150].w[13]" 0.00014564334094097807;
	setAttr ".wl[150].w[14]" 0.002399355341554648;
	setAttr ".wl[150].w[15]" 0.00018437792470635608;
	setAttr ".wl[150].w[18]" 0.98759228005403921;
	setAttr ".wl[150].w[19]" 0.0096783433387588793;
	setAttr -s 5 ".wl[151].w";
	setAttr ".wl[151].w[13]" 0.0033644347789367353;
	setAttr ".wl[151].w[14]" 0.0068886992059756348;
	setAttr ".wl[151].w[15]" 0.011765806566999579;
	setAttr ".wl[151].w[18]" 0.95848458622342603;
	setAttr ".wl[151].w[19]" 0.01949647322466207;
	setAttr -s 5 ".wl[152].w";
	setAttr ".wl[152].w[14]" 0.000765933883197332;
	setAttr ".wl[152].w[15]" 0.068682343154988237;
	setAttr ".wl[152].w[16]" 0.0051782595776260851;
	setAttr ".wl[152].w[18]" 0.91146840449291155;
	setAttr ".wl[152].w[19]" 0.013905058891276733;
	setAttr -s 4 ".wl[153].w";
	setAttr ".wl[153].w[13]" 0.075648354685108304;
	setAttr ".wl[153].w[14]" 0.56277707291252632;
	setAttr ".wl[153].w[15]" 0.12544109968291897;
	setAttr ".wl[153].w[18]" 0.23613347271944651;
	setAttr -s 4 ".wl[154].w";
	setAttr ".wl[154].w[13]" 5.4366064093715647e-05;
	setAttr ".wl[154].w[14]" 0.33172909748583429;
	setAttr ".wl[154].w[15]" 0.14084936182467528;
	setAttr ".wl[154].w[18]" 0.52736717462539673;
	setAttr -s 3 ".wl[155].w[14:16]"  0.5364792547262679 0.42972444287222639 0.033796302401505669;
	setAttr -s 3 ".wl[156].w[13:15]"  0.10336888779912393 0.81358131770917819 0.083049794491697956;
	setAttr -s 4 ".wl[157].w";
	setAttr ".wl[157].w[14]" 0.50097533860418453;
	setAttr ".wl[157].w[15]" 0.36158145963130334;
	setAttr ".wl[157].w[16]" 0.038752825390695009;
	setAttr ".wl[157].w[18]" 0.098690376373817001;
	setAttr -s 5 ".wl[158].w";
	setAttr ".wl[158].w[14]" 0.014796965735851614;
	setAttr ".wl[158].w[15]" 0.029808310898918167;
	setAttr ".wl[158].w[16]" 0.0079522955816263147;
	setAttr ".wl[158].w[18]" 0.91435962855386932;
	setAttr ".wl[158].w[19]" 0.033082799229734561;
	setAttr -s 3 ".wl[159].w";
	setAttr ".wl[159].w[14]" 0.14575895897316804;
	setAttr ".wl[159].w[15]" 0.10420772203040252;
	setAttr ".wl[159].w[18]" 0.75003331899642944;
	setAttr ".wl[160].w[14]"  1;
	setAttr -s 2 ".wl[161].w";
	setAttr ".wl[161].w[14]" 0.81106948681899538;
	setAttr ".wl[161].w[18]" 0.18893051318100473;
	setAttr -s 2 ".wl[162].w";
	setAttr ".wl[162].w[14]" 0.24381059587496545;
	setAttr ".wl[162].w[18]" 0.75618940412503477;
	setAttr -s 3 ".wl[163].w";
	setAttr ".wl[163].w[14]" 0.051392168511984283;
	setAttr ".wl[163].w[18]" 0.79749435186386108;
	setAttr ".wl[163].w[19]" 0.15111347962415464;
	setAttr -s 2 ".wl[164].w[18:19]"  0.64730374467734597 0.35269625532265397;
	setAttr -s 2 ".wl[165].w[18:19]"  0.58377916367760929 0.41622083632239071;
	setAttr -s 2 ".wl[166].w[18:19]"  0.59727393180603017 0.40272606819396983;
	setAttr -s 4 ".wl[167].w";
	setAttr ".wl[167].w[14]" 0.0028316110845266998;
	setAttr ".wl[167].w[15]" 0.0020193830078666783;
	setAttr ".wl[167].w[18]" 0.97955604407083685;
	setAttr ".wl[167].w[19]" 0.015592961836769764;
	setAttr -s 3 ".wl[168].w";
	setAttr ".wl[168].w[15]" 0.0095408415492658598;
	setAttr ".wl[168].w[18]" 0.97491672078804315;
	setAttr ".wl[168].w[19]" 0.015542437662691064;
	setAttr -s 2 ".wl[169].w[18:19]"  0.55917374855832447 0.44082625144167559;
	setAttr -s 2 ".wl[170].w[18:19]"  0.7487472993031582 0.25125270069684169;
	setAttr -s 3 ".wl[171].w[14:16]"  0.031980608433097954 0.44777040967994414 0.5202489818869579;
	setAttr -s 3 ".wl[172].w[14:16]"  0.23227701397390371 0.72857982470461102 0.039143161321485313;
	setAttr -s 3 ".wl[173].w[14:16]"  0.55329193531170695 0.41841689460235576 0.028291170085937279;
	setAttr -s 3 ".wl[174].w[13:15]"  0.100558037094878 0.82723918959892284 0.072202773306199106;
	setAttr -s 2 ".wl[175].w";
	setAttr ".wl[175].w[16]" 1;
	setAttr ".wl[175].w[26]" 0.022535125296426543;
	setAttr ".wl[176].w[16]"  1;
	setAttr ".wl[177].w[16]"  1;
	setAttr ".wl[178].w[16]"  1;
	setAttr -s 2 ".wl[179].w";
	setAttr ".wl[179].w[16]" 1;
	setAttr ".wl[179].w[26]" 0.026283013464431539;
	setAttr -s 2 ".wl[180].w";
	setAttr ".wl[180].w[16]" 1;
	setAttr ".wl[180].w[26]" 0.023307239416581943;
	setAttr -s 2 ".wl[181].w";
	setAttr ".wl[181].w[16]" 1;
	setAttr ".wl[181].w[26]" 0.016990650063128245;
	setAttr ".wl[182].w[16]"  1.0000000000000002;
	setAttr ".wl[183].w[16]"  1;
	setAttr ".wl[184].w[16]"  1;
	setAttr -s 2 ".wl[185].w";
	setAttr ".wl[185].w[16]" 1;
	setAttr ".wl[185].w[26]" 0.0157848376107322;
	setAttr ".wl[186].w[16]"  1;
	setAttr ".wl[187].w[16]"  1;
	setAttr ".wl[188].w[16]"  0.99999999999999989;
	setAttr -s 2 ".wl[189].w";
	setAttr ".wl[189].w[16]" 1;
	setAttr ".wl[189].w[26]" 0.018477003824855506;
	setAttr -s 2 ".wl[190].w";
	setAttr ".wl[190].w[16]" 1;
	setAttr ".wl[190].w[26]" 0.018095710030472133;
	setAttr -s 2 ".wl[191].w";
	setAttr ".wl[191].w[16]" 1;
	setAttr ".wl[191].w[26]" 0.013525458985481882;
	setAttr ".wl[192].w[16]"  1;
	setAttr ".wl[193].w[16]"  1;
	setAttr ".wl[194].w[16]"  1;
	setAttr ".wl[195].w[16]"  1;
	setAttr -s 2 ".wl[196].w";
	setAttr ".wl[196].w[16]" 1;
	setAttr ".wl[196].w[26]" 0.010270058051056016;
	setAttr -s 2 ".wl[197].w";
	setAttr ".wl[197].w[16]" 1;
	setAttr ".wl[197].w[26]" 0.14491246093148327;
	setAttr -s 2 ".wl[198].w";
	setAttr ".wl[198].w[16]" 1;
	setAttr ".wl[198].w[26]" 0.18173997678770323;
	setAttr -s 2 ".wl[199].w";
	setAttr ".wl[199].w[16]" 1;
	setAttr ".wl[199].w[26]" 0.16996845869136598;
	setAttr -s 2 ".wl[200].w";
	setAttr ".wl[200].w[16]" 1;
	setAttr ".wl[200].w[26]" 0.17644768790425372;
	setAttr -s 2 ".wl[201].w";
	setAttr ".wl[201].w[16]" 1;
	setAttr ".wl[201].w[26]" 0.054058457577610269;
	setAttr -s 2 ".wl[202].w";
	setAttr ".wl[202].w[16]" 1;
	setAttr ".wl[202].w[26]" 0.057080216076001583;
	setAttr -s 2 ".wl[203].w";
	setAttr ".wl[203].w[16]" 1;
	setAttr ".wl[203].w[26]" 0.065558510113542412;
	setAttr -s 2 ".wl[204].w";
	setAttr ".wl[204].w[16]" 1;
	setAttr ".wl[204].w[26]" 0.064317350329749223;
	setAttr -s 2 ".wl[205].w";
	setAttr ".wl[205].w[16]" 1;
	setAttr ".wl[205].w[26]" 0.32512454041145761;
	setAttr -s 2 ".wl[206].w";
	setAttr ".wl[206].w[16]" 1;
	setAttr ".wl[206].w[26]" 0.53817530377648226;
	setAttr -s 2 ".wl[207].w";
	setAttr ".wl[207].w[16]" 1;
	setAttr ".wl[207].w[26]" 0.31286691271089334;
	setAttr -s 2 ".wl[208].w";
	setAttr ".wl[208].w[16]" 1;
	setAttr ".wl[208].w[26]" 0.27264884634744219;
	setAttr -s 2 ".wl[209].w";
	setAttr ".wl[209].w[16]" 1;
	setAttr ".wl[209].w[26]" 0.14183794858824977;
	setAttr -s 2 ".wl[210].w";
	setAttr ".wl[210].w[16]" 1;
	setAttr ".wl[210].w[26]" 0.16014721415775138;
	setAttr -s 2 ".wl[211].w";
	setAttr ".wl[211].w[16]" 1;
	setAttr ".wl[211].w[26]" 0.4227642635263002;
	setAttr -s 2 ".wl[212].w";
	setAttr ".wl[212].w[16]" 1;
	setAttr ".wl[212].w[26]" 0.26450931823590429;
	setAttr -s 2 ".wl[213].w";
	setAttr ".wl[213].w[16]" 1;
	setAttr ".wl[213].w[26]" 0.1274457677969941;
	setAttr -s 2 ".wl[214].w";
	setAttr ".wl[214].w[16]" 1;
	setAttr ".wl[214].w[26]" 0.087457663692177834;
	setAttr -s 2 ".wl[215].w";
	setAttr ".wl[215].w[16]" 1;
	setAttr ".wl[215].w[26]" 0.093211883899810041;
	setAttr -s 2 ".wl[216].w";
	setAttr ".wl[216].w[16]" 1;
	setAttr ".wl[216].w[26]" 0.12399115592896176;
	setAttr -s 2 ".wl[217].w";
	setAttr ".wl[217].w[16]" 1;
	setAttr ".wl[217].w[26]" 0.20849312236172651;
	setAttr -s 2 ".wl[218].w";
	setAttr ".wl[218].w[16]" 1;
	setAttr ".wl[218].w[26]" 0.076009851597341013;
	setAttr -s 2 ".wl[219].w";
	setAttr ".wl[219].w[16]" 1;
	setAttr ".wl[219].w[26]" 0.075929007658322015;
	setAttr -s 2 ".wl[220].w";
	setAttr ".wl[220].w[16]" 1;
	setAttr ".wl[220].w[26]" 0.096994354116435533;
	setAttr -s 2 ".wl[221].w";
	setAttr ".wl[221].w[16]" 1;
	setAttr ".wl[221].w[26]" 0.14118354470068206;
	setAttr -s 2 ".wl[222].w";
	setAttr ".wl[222].w[16]" 1;
	setAttr ".wl[222].w[26]" 0.057343300105560283;
	setAttr -s 2 ".wl[223].w";
	setAttr ".wl[223].w[16]" 1;
	setAttr ".wl[223].w[26]" 0.049014369532650121;
	setAttr ".wl[224].w[16]"  1;
	setAttr ".wl[225].w[16]"  0.99999999999999989;
	setAttr ".wl[226].w[16]"  1;
	setAttr -s 2 ".wl[227].w";
	setAttr ".wl[227].w[16]" 1;
	setAttr ".wl[227].w[26]" 0.053415827733934343;
	setAttr -s 2 ".wl[228].w";
	setAttr ".wl[228].w[16]" 1;
	setAttr ".wl[228].w[26]" 0.04649832247234225;
	setAttr ".wl[229].w[16]"  1;
	setAttr ".wl[230].w[16]"  1;
	setAttr ".wl[231].w[16]"  1;
	setAttr -s 2 ".wl[232].w";
	setAttr ".wl[232].w[16]" 1;
	setAttr ".wl[232].w[26]" 0.22175205056321667;
	setAttr -s 2 ".wl[233].w";
	setAttr ".wl[233].w[16]" 1;
	setAttr ".wl[233].w[26]" 0.16702319524850845;
	setAttr -s 2 ".wl[234].w";
	setAttr ".wl[234].w[16]" 1;
	setAttr ".wl[234].w[26]" 0.099946329715097884;
	setAttr -s 2 ".wl[235].w";
	setAttr ".wl[235].w[16]" 1;
	setAttr ".wl[235].w[26]" 0.13403434006702586;
	setAttr -s 2 ".wl[236].w";
	setAttr ".wl[236].w[16]" 1;
	setAttr ".wl[236].w[26]" 0.11507158443821676;
	setAttr -s 2 ".wl[237].w";
	setAttr ".wl[237].w[16]" 1;
	setAttr ".wl[237].w[26]" 0.095340003791676314;
	setAttr -s 2 ".wl[238].w";
	setAttr ".wl[238].w[16]" 1;
	setAttr ".wl[238].w[26]" 0.084211168894444244;
	setAttr -s 2 ".wl[239].w";
	setAttr ".wl[239].w[16]" 1;
	setAttr ".wl[239].w[26]" 0.069936627097305054;
	setAttr -s 2 ".wl[240].w";
	setAttr ".wl[240].w[16]" 1;
	setAttr ".wl[240].w[26]" 0.056635925990565751;
	setAttr -s 2 ".wl[241].w";
	setAttr ".wl[241].w[16]" 1;
	setAttr ".wl[241].w[26]" 0.053445512379637197;
	setAttr -s 2 ".wl[242].w";
	setAttr ".wl[242].w[16]" 1;
	setAttr ".wl[242].w[26]" 0.061109769556976286;
	setAttr ".wl[243].w[16]"  1;
	setAttr ".wl[244].w[16]"  1;
	setAttr ".wl[245].w[16]"  1;
	setAttr -s 2 ".wl[246].w";
	setAttr ".wl[246].w[16]" 1;
	setAttr ".wl[246].w[26]" 0.032865042127564172;
	setAttr ".wl[247].w[16]"  1;
	setAttr -s 3 ".wl[248].w[14:16]"  0.015452857914958748 0.021605237853039031 0.96294190423200221;
	setAttr -s 2 ".wl[249].w";
	setAttr ".wl[249].w[16]" 1;
	setAttr ".wl[249].w[26]" 0.077226152337212722;
	setAttr -s 2 ".wl[250].w";
	setAttr ".wl[250].w[16]" 1;
	setAttr ".wl[250].w[26]" 0.22539871142580836;
	setAttr -s 2 ".wl[251].w";
	setAttr ".wl[251].w[16]" 1;
	setAttr ".wl[251].w[26]" 0.42500622353836959;
	setAttr -s 2 ".wl[252].w";
	setAttr ".wl[252].w[16]" 1;
	setAttr ".wl[252].w[26]" 0.58086445740599424;
	setAttr -s 2 ".wl[253].w";
	setAttr ".wl[253].w[16]" 1;
	setAttr ".wl[253].w[26]" 0.073190963802867035;
	setAttr -s 2 ".wl[254].w";
	setAttr ".wl[254].w[16]" 1;
	setAttr ".wl[254].w[26]" 0.063236448723882316;
	setAttr -s 2 ".wl[255].w";
	setAttr ".wl[255].w[16]" 1;
	setAttr ".wl[255].w[26]" 0.05526449556050507;
	setAttr -s 2 ".wl[256].w";
	setAttr ".wl[256].w[16]" 1;
	setAttr ".wl[256].w[26]" 0.054678102870320898;
	setAttr -s 2 ".wl[257].w";
	setAttr ".wl[257].w[16]" 1;
	setAttr ".wl[257].w[26]" 0.064442986968640703;
	setAttr -s 2 ".wl[258].w";
	setAttr ".wl[258].w[16]" 1;
	setAttr ".wl[258].w[26]" 0.016007854781701004;
	setAttr -s 2 ".wl[259].w";
	setAttr ".wl[259].w[16]" 1;
	setAttr ".wl[259].w[26]" 0.01655165513077192;
	setAttr -s 2 ".wl[260].w";
	setAttr ".wl[260].w[16]" 1;
	setAttr ".wl[260].w[26]" 0.010041257873585436;
	setAttr -s 2 ".wl[261].w";
	setAttr ".wl[261].w[16]" 1;
	setAttr ".wl[261].w[26]" 0.0087982501753074444;
	setAttr ".wl[262].w[16]"  1;
	setAttr ".wl[263].w[16]"  1;
	setAttr ".wl[264].w[16]"  1;
	setAttr ".wl[265].w[16]"  1;
	setAttr -s 2 ".wl[266].w";
	setAttr ".wl[266].w[16]" 1;
	setAttr ".wl[266].w[26]" 0.029786091912691461;
	setAttr -s 2 ".wl[267].w";
	setAttr ".wl[267].w[16]" 1;
	setAttr ".wl[267].w[26]" 0.024822132968059199;
	setAttr -s 2 ".wl[268].w";
	setAttr ".wl[268].w[16]" 1;
	setAttr ".wl[268].w[26]" 0.055998820094083621;
	setAttr -s 2 ".wl[269].w";
	setAttr ".wl[269].w[16]" 1;
	setAttr ".wl[269].w[26]" 0.034936967881675551;
	setAttr -s 2 ".wl[270].w";
	setAttr ".wl[270].w[16]" 1;
	setAttr ".wl[270].w[26]" 0.089921133329761857;
	setAttr -s 2 ".wl[271].w";
	setAttr ".wl[271].w[16]" 1;
	setAttr ".wl[271].w[26]" 0.11520476059451668;
	setAttr -s 2 ".wl[272].w";
	setAttr ".wl[272].w[16]" 1;
	setAttr ".wl[272].w[26]" 0.13551946628132908;
	setAttr -s 2 ".wl[273].w";
	setAttr ".wl[273].w[16]" 1;
	setAttr ".wl[273].w[26]" 0.084458022687044623;
	setAttr -s 2 ".wl[274].w";
	setAttr ".wl[274].w[16]" 1;
	setAttr ".wl[274].w[26]" 0.51978331833426605;
	setAttr -s 2 ".wl[275].w";
	setAttr ".wl[275].w[16]" 1;
	setAttr ".wl[275].w[26]" 0.029630674713159569;
	setAttr -s 2 ".wl[276].w";
	setAttr ".wl[276].w[16]" 1;
	setAttr ".wl[276].w[26]" 0.013564397948035453;
	setAttr -s 2 ".wl[277].w";
	setAttr ".wl[277].w[16]" 1;
	setAttr ".wl[277].w[26]" 0.0018847906730508415;
	setAttr -s 2 ".wl[278].w";
	setAttr ".wl[278].w[16]" 1;
	setAttr ".wl[278].w[26]" 0.01243222568513801;
	setAttr -s 2 ".wl[279].w";
	setAttr ".wl[279].w[16]" 1;
	setAttr ".wl[279].w[26]" 0.0056279402924768037;
	setAttr -s 2 ".wl[280].w";
	setAttr ".wl[280].w[16]" 1;
	setAttr ".wl[280].w[26]" 0.0015961177913317998;
	setAttr -s 2 ".wl[281].w";
	setAttr ".wl[281].w[16]" 1;
	setAttr ".wl[281].w[26]" 0.0080402405883582811;
	setAttr -s 2 ".wl[282].w";
	setAttr ".wl[282].w[16]" 1;
	setAttr ".wl[282].w[26]" 0.0084944323947315336;
	setAttr -s 2 ".wl[283].w";
	setAttr ".wl[283].w[16]" 1;
	setAttr ".wl[283].w[26]" 0.0074445922448853471;
	setAttr ".wl[284].w[16]"  1;
	setAttr ".wl[285].w[16]"  1;
	setAttr ".wl[286].w[16]"  1;
	setAttr ".wl[287].w[16]"  0.99999999999999989;
	setAttr ".wl[288].w[16]"  1;
	setAttr ".wl[289].w[16]"  1;
	setAttr -s 2 ".wl[290].w";
	setAttr ".wl[290].w[16]" 1;
	setAttr ".wl[290].w[26]" 0.33190610378635693;
	setAttr -s 2 ".wl[291].w";
	setAttr ".wl[291].w[16]" 1;
	setAttr ".wl[291].w[26]" 0.16703979298311988;
	setAttr -s 2 ".wl[292].w";
	setAttr ".wl[292].w[16]" 1;
	setAttr ".wl[292].w[26]" 0.021881121672221403;
	setAttr ".wl[293].w[16]"  1;
	setAttr ".wl[294].w[16]"  1;
	setAttr ".wl[295].w[16]"  1;
	setAttr -s 3 ".wl[296].w[14:16]"  0.26627386053670843 0.60603253378011079 0.12769360568318075;
	setAttr -s 4 ".wl[297].w";
	setAttr ".wl[297].w[14]" 0.16021647690185753;
	setAttr ".wl[297].w[15]" 0.52994462147353605;
	setAttr ".wl[297].w[16]" 0.20511018799297653;
	setAttr ".wl[297].w[24]" 0.10472871363162994;
	setAttr -s 3 ".wl[298].w[14:16]"  0.060280940503856739 0.1509278266486036 0.7887912328475396;
	setAttr -s 3 ".wl[299].w[14:16]"  0.1198713756291616 0.3783932531641005 0.50173537120673795;
	setAttr -s 3 ".wl[300].w[14:16]"  0.34531721619262895 0.59749197862066727 0.057190805186703782;
	setAttr -s 3 ".wl[301].w[14:16]"  0.054171957421806936 0.096376098671763194 0.84945194390642997;
	setAttr -s 4 ".wl[302].w";
	setAttr ".wl[302].w[14]" 0.25183573912661494;
	setAttr ".wl[302].w[15]" 0.2439354660499892;
	setAttr ".wl[302].w[16]" 0.10774608912673324;
	setAttr ".wl[302].w[24]" 0.39648270569666255;
	setAttr -s 4 ".wl[303].w";
	setAttr ".wl[303].w[14]" 0.086105840534546785;
	setAttr ".wl[303].w[15]" 0.11552997106444776;
	setAttr ".wl[303].w[16]" 0.014550301367010412;
	setAttr ".wl[303].w[24]" 0.78381388703399502;
	setAttr -s 3 ".wl[304].w[14:16]"  0.054167711627198238 0.10654004366508826 0.83929224470771346;
	setAttr -s 3 ".wl[305].w[14:16]"  0.062630464410136658 0.20963922281139491 0.72773031277846845;
	setAttr -s 3 ".wl[306].w[14:16]"  0.035431506183265016 0.42800900774146489 0.53655948607527015;
	setAttr -s 3 ".wl[307].w[14:16]"  0.021062580357801456 0.52358156744234974 0.4553558521998487;
	setAttr -s 4 ".wl[308].w";
	setAttr ".wl[308].w[14]" 0.16784168002402597;
	setAttr ".wl[308].w[15]" 0.51238267295091522;
	setAttr ".wl[308].w[16]" 0.17868325720305256;
	setAttr ".wl[308].w[24]" 0.14109238982200625;
	setAttr -s 4 ".wl[309].w";
	setAttr ".wl[309].w[14]" 0.23080236115175295;
	setAttr ".wl[309].w[15]" 0.47868535745887031;
	setAttr ".wl[309].w[16]" 0.088212224574229281;
	setAttr ".wl[309].w[24]" 0.2023000568151474;
	setAttr -s 4 ".wl[310].w";
	setAttr ".wl[310].w[14]" 0.21895397473224465;
	setAttr ".wl[310].w[15]" 0.63817876076784064;
	setAttr ".wl[310].w[16]" 0.076810275366556699;
	setAttr ".wl[310].w[24]" 0.066056989133358002;
	setAttr -s 3 ".wl[311].w[14:16]"  0.19918275196709417 0.74856346643638205 0.052253781596523677;
	setAttr -s 4 ".wl[312].w";
	setAttr ".wl[312].w[14]" 0.50388731514103913;
	setAttr ".wl[312].w[15]" 0.2981244252043363;
	setAttr ".wl[312].w[16]" 0.0070188669973446473;
	setAttr ".wl[312].w[24]" 0.19096939265727997;
	setAttr -s 4 ".wl[313].w";
	setAttr ".wl[313].w[14]" 0.29572839267051221;
	setAttr ".wl[313].w[15]" 0.25618811991588375;
	setAttr ".wl[313].w[16]" 0.00096779789753655317;
	setAttr ".wl[313].w[24]" 0.4471156895160675;
	setAttr -s 4 ".wl[314].w";
	setAttr ".wl[314].w[14]" 0.17928409044979579;
	setAttr ".wl[314].w[15]" 0.21301051675729168;
	setAttr ".wl[314].w[16]" 0.1070531987697802;
	setAttr ".wl[314].w[24]" 0.50065219402313232;
	setAttr -s 4 ".wl[315].w";
	setAttr ".wl[315].w[14]" 0.17139559847824715;
	setAttr ".wl[315].w[15]" 0.2326783381405354;
	setAttr ".wl[315].w[16]" 0.11575557502367344;
	setAttr ".wl[315].w[24]" 0.48017048835754395;
	setAttr -s 4 ".wl[316].w";
	setAttr ".wl[316].w[14]" 0.12677276280634434;
	setAttr ".wl[316].w[15]" 0.21217953501267775;
	setAttr ".wl[316].w[16]" 0.082470362531777405;
	setAttr ".wl[316].w[24]" 0.57857733964920044;
	setAttr -s 2 ".wl[317].w";
	setAttr ".wl[317].w[14]" 0.69198344383823573;
	setAttr ".wl[317].w[24]" 0.30801655616176421;
	setAttr -s 2 ".wl[318].w";
	setAttr ".wl[318].w[14]" 0.17063543567757805;
	setAttr ".wl[318].w[24]" 0.829364564322422;
	setAttr -s 5 ".wl[319].w";
	setAttr ".wl[319].w[13]" 0.0021054130918368081;
	setAttr ".wl[319].w[14]" 0.041175516459536161;
	setAttr ".wl[319].w[15]" 0.002663131287327859;
	setAttr ".wl[319].w[24]" 0.73854321241378784;
	setAttr ".wl[319].w[25]" 0.21551272674751135;
	setAttr -s 5 ".wl[320].w";
	setAttr ".wl[320].w[13]" 0.026382164513285209;
	setAttr ".wl[320].w[14]" 0.053902505487325718;
	setAttr ".wl[320].w[15]" 0.097941517794081903;
	setAttr ".wl[320].w[24]" 0.65448158979415894;
	setAttr ".wl[320].w[25]" 0.16729222241114824;
	setAttr -s 5 ".wl[321].w";
	setAttr ".wl[321].w[14]" 0.0062469981410792127;
	setAttr ".wl[321].w[15]" 0.14146255522945936;
	setAttr ".wl[321].w[16]" 0.01878957516349538;
	setAttr ".wl[321].w[24]" 0.77006471157073964;
	setAttr ".wl[321].w[25]" 0.063436159895226302;
	setAttr -s 4 ".wl[322].w";
	setAttr ".wl[322].w[13]" 0.075648354685108304;
	setAttr ".wl[322].w[14]" 0.56277707291252632;
	setAttr ".wl[322].w[15]" 0.12544109968291894;
	setAttr ".wl[322].w[24]" 0.23613347271944651;
	setAttr -s 3 ".wl[323].w";
	setAttr ".wl[323].w[14]" 0.23150108576106757;
	setAttr ".wl[323].w[15]" 0.10478499245128362;
	setAttr ".wl[323].w[24]" 0.66371392178764876;
	setAttr -s 3 ".wl[324].w[14:16]"  0.53647925474133107 0.42972444361757095 0.033796301641098148;
	setAttr -s 3 ".wl[325].w[13:15]"  0.10336889152612032 0.81358132507453884 0.083049783399341062;
	setAttr -s 4 ".wl[326].w";
	setAttr ".wl[326].w[14]" 0.49405748773341129;
	setAttr ".wl[326].w[15]" 0.36135419252654688;
	setAttr ".wl[326].w[16]" 0.037971627797269279;
	setAttr ".wl[326].w[24]" 0.1066166919427726;
	setAttr -s 5 ".wl[327].w";
	setAttr ".wl[327].w[14]" 0.043691149806963647;
	setAttr ".wl[327].w[15]" 0.064704713843006426;
	setAttr ".wl[327].w[16]" 0.023513868957409523;
	setAttr ".wl[327].w[24]" 0.73311895132064819;
	setAttr ".wl[327].w[25]" 0.13497131607197224;
	setAttr -s 3 ".wl[328].w";
	setAttr ".wl[328].w[14]" 0.077764163145406268;
	setAttr ".wl[328].w[15]" 0.056733743940560029;
	setAttr ".wl[328].w[24]" 0.86550209291403379;
	setAttr -s 2 ".wl[329].w";
	setAttr ".wl[329].w[14]" 0.81106997844289508;
	setAttr ".wl[329].w[24]" 0.18893002155710495;
	setAttr -s 2 ".wl[330].w";
	setAttr ".wl[330].w[14]" 0.24381095079062143;
	setAttr ".wl[330].w[24]" 0.75618904920937857;
	setAttr -s 3 ".wl[331].w";
	setAttr ".wl[331].w[14]" 0.07228107278001257;
	setAttr ".wl[331].w[24]" 0.71518373489379883;
	setAttr ".wl[331].w[25]" 0.21253519232618859;
	setAttr -s 2 ".wl[332].w[24:25]"  0.64734160900115967 0.35265839099884033;
	setAttr -s 2 ".wl[333].w[24:25]"  0.58230836731891256 0.41769163268108744;
	setAttr -s 2 ".wl[334].w[24:25]"  0.59422730929164502 0.40577269070835498;
	setAttr -s 4 ".wl[335].w";
	setAttr ".wl[335].w[14]" 0.0054099104310805076;
	setAttr ".wl[335].w[15]" 0.0038584683117531778;
	setAttr ".wl[335].w[24]" 0.86976832151412964;
	setAttr ".wl[335].w[25]" 0.12096329974303668;
	setAttr -s 3 ".wl[336].w";
	setAttr ".wl[336].w[15]" 0.050212595750161751;
	setAttr ".wl[336].w[24]" 0.76122355461120605;
	setAttr ".wl[336].w[25]" 0.18856384963863215;
	setAttr -s 2 ".wl[337].w[24:25]"  0.5541454883062813 0.44585451169371865;
	setAttr -s 2 ".wl[338].w[24:25]"  0.74588278852027823 0.25411721147972188;
	setAttr -s 2 ".wl[339].w";
	setAttr ".wl[339].w[16]" 1;
	setAttr ".wl[339].w[26]" 0.022535121826941722;
	setAttr ".wl[340].w[16]"  1;
	setAttr ".wl[341].w[16]"  1;
	setAttr ".wl[342].w[16]"  0.99999999999999989;
	setAttr -s 2 ".wl[343].w";
	setAttr ".wl[343].w[16]" 1;
	setAttr ".wl[343].w[26]" 0.02628301346443156;
	setAttr -s 2 ".wl[344].w";
	setAttr ".wl[344].w[16]" 1;
	setAttr ".wl[344].w[26]" 0.023307242892307508;
	setAttr -s 2 ".wl[345].w";
	setAttr ".wl[345].w[16]" 1;
	setAttr ".wl[345].w[26]" 0.016990650063128256;
	setAttr ".wl[346].w[16]"  1;
	setAttr ".wl[347].w[16]"  1;
	setAttr ".wl[348].w[16]"  1;
	setAttr -s 2 ".wl[349].w";
	setAttr ".wl[349].w[16]" 1;
	setAttr ".wl[349].w[26]" 0.015784834789143949;
	setAttr ".wl[350].w[16]"  1;
	setAttr ".wl[351].w[16]"  1;
	setAttr ".wl[352].w[16]"  0.99999999999999989;
	setAttr -s 2 ".wl[353].w";
	setAttr ".wl[353].w[16]" 1;
	setAttr ".wl[353].w[26]" 0.018477003824855516;
	setAttr -s 2 ".wl[354].w";
	setAttr ".wl[354].w[16]" 1;
	setAttr ".wl[354].w[26]" 0.018095710030472143;
	setAttr -s 2 ".wl[355].w";
	setAttr ".wl[355].w[16]" 1;
	setAttr ".wl[355].w[26]" 0.013525458985481888;
	setAttr ".wl[356].w[16]"  1;
	setAttr ".wl[357].w[16]"  1;
	setAttr ".wl[358].w[16]"  0.99999999999999989;
	setAttr ".wl[359].w[16]"  1;
	setAttr -s 2 ".wl[360].w";
	setAttr ".wl[360].w[16]" 1;
	setAttr ".wl[360].w[26]" 0.010270058051056024;
	setAttr -s 2 ".wl[361].w";
	setAttr ".wl[361].w[16]" 1;
	setAttr ".wl[361].w[26]" 0.1449124599670924;
	setAttr -s 2 ".wl[362].w";
	setAttr ".wl[362].w[16]" 1;
	setAttr ".wl[362].w[26]" 0.88466287696646306;
	setAttr -s 2 ".wl[363].w";
	setAttr ".wl[363].w[16]" 1;
	setAttr ".wl[363].w[26]" 0.81383157675388307;
	setAttr -s 2 ".wl[364].w";
	setAttr ".wl[364].w[16]" 1;
	setAttr ".wl[364].w[26]" 0.8088622080169372;
	setAttr -s 2 ".wl[365].w";
	setAttr ".wl[365].w[16]" 1;
	setAttr ".wl[365].w[26]" 0.88274202846747196;
	setAttr -s 2 ".wl[366].w";
	setAttr ".wl[366].w[16]" 1;
	setAttr ".wl[366].w[26]" 0.78949767333130638;
	setAttr -s 2 ".wl[367].w";
	setAttr ".wl[367].w[16]" 1;
	setAttr ".wl[367].w[26]" 0.86071999082742645;
	setAttr -s 2 ".wl[368].w";
	setAttr ".wl[368].w[16]" 1;
	setAttr ".wl[368].w[26]" 0.73975821849002565;
	setAttr -s 2 ".wl[369].w";
	setAttr ".wl[369].w[16]" 1;
	setAttr ".wl[369].w[26]" 0.78447598725382961;
	setAttr -s 2 ".wl[370].w";
	setAttr ".wl[370].w[16]" 1;
	setAttr ".wl[370].w[26]" 0.88274202846747196;
	setAttr -s 2 ".wl[371].w";
	setAttr ".wl[371].w[16]" 1;
	setAttr ".wl[371].w[26]" 0.8088622080169372;
	setAttr -s 2 ".wl[372].w";
	setAttr ".wl[372].w[16]" 1;
	setAttr ".wl[372].w[26]" 0.86071999427317536;
	setAttr -s 2 ".wl[373].w";
	setAttr ".wl[373].w[16]" 1;
	setAttr ".wl[373].w[26]" 0.78949767333130638;
	setAttr -s 2 ".wl[374].w";
	setAttr ".wl[374].w[16]" 1;
	setAttr ".wl[374].w[26]" 0.78447599858835804;
	setAttr -s 2 ".wl[375].w";
	setAttr ".wl[375].w[16]" 1;
	setAttr ".wl[375].w[26]" 0.73975821849002543;
	setAttr -s 30 ".pm";
	setAttr ".pm[0]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -8.9231745720989668 0.17376929722515433 2.0199273074892598e-15 1;
	setAttr ".pm[1]" -type "matrix" -3.4450928483976665e-16 -2.2204460492503131e-16 -1 0 -1 4.9303806576313238e-32 3.4450928483976665e-16 0
		 -7.6496428045251064e-32 1 -2.2204460492503131e-16 0 8.9231745720989668 0.17376929722515455 0.999999999999997 1;
	setAttr ".pm[2]" -type "matrix" -3.4450928483976665e-16 -2.2204460492503131e-16 -1 0 -1 4.9303806576313238e-32 3.4450928483976665e-16 0
		 -7.6496428045251064e-32 1 -2.2204460492503131e-16 0 4.6515061293712359 0.17376929722515452 0.99999999999999889 1;
	setAttr ".pm[3]" -type "matrix" 5.8331365260285766e-07 -3.4717393473770988e-07 -0.99999999999976963 0 -0.4794097213532717 0.87759120270866275 -5.8432302659159539e-07 0
		 0.87759120270866331 0.47940972135350218 3.454723706304003e-07 0 0.53189973592848949 -0.61121325699033013 1.0000005224619188 1;
	setAttr ".pm[4]" -type "matrix" -3.7839275046629232e-09 -4.9514660478913824e-07 -0.99999999999987765 0 4.5717040610908244e-16 0.99999999999987776 -4.9514660478913814e-07 0
		 1.0000000000000002 -2.2981828101998501e-15 -3.7839275046623533e-09 0 -1.0271901970466448 -0.13533431203966553 1.0000008717993354 1;
	setAttr ".pm[5]" -type "matrix" -3.7839275046629232e-09 -4.9514660478913824e-07 -0.99999999999987765 0 4.5717040610908244e-16 0.99999999999987776 -4.9514660478913814e-07 0
		 1.0000000000000002 -2.2981828101998501e-15 -3.7839275046623533e-09 0 -1.8935622781747257 -0.1353343120396657 1.0000008717993347 1;
	setAttr ".pm[6]" -type "matrix" 2.2204460492503131e-16 9.9579925010295987e-17 -1 0 1 -2.2111185107375414e-32 2.2204460492503131e-16 0
		 4.9303806576313238e-32 -1 -9.9579925010295987e-17 0 -8.9231700000000007 -0.1737689999999999 -1.000000000000002 1;
	setAttr ".pm[7]" -type "matrix" 2.2204460492503131e-16 9.9579925010295987e-17 -1 0 1 -2.2111185107375414e-32 2.2204460492503131e-16 0
		 4.9303806576313238e-32 -1 -9.9579925010295987e-17 0 -4.65151 -0.1737689999999999 -1.0000000000000011 1;
	setAttr ".pm[8]" -type "matrix" 5.8331365260285766e-07 -3.4602377056398311e-07 -0.99999999999976996 0 0.47940972135327098 -0.87759120270866364 5.8331365263106153e-07 0
		 -0.87759120270866364 -0.47940972135350091 -3.460237705164382e-07 0 -0.53189953941047974 0.61121351838277305 -1.0000005217588994 1;
	setAttr ".pm[9]" -type "matrix" -3.7839275046628231e-09 -5.0889760207317231e-07 -0.99999999999987077 0 -5.094072503275622e-16 -0.99999999999987077 5.0889760207317231e-07 0
		 -1 2.5476401720380396e-15 3.7839275046620083e-09 0 1.0271899962160689 0.13533449110186921 -1.0000010727583399 1;
	setAttr ".pm[10]" -type "matrix" -3.7839275046628231e-09 -5.0889760207317231e-07 -0.99999999999987077 0 -5.094072503275622e-16 -0.99999999999987077 5.0889760207317231e-07 0
		 -1 2.5476401720380396e-15 3.7839275046620083e-09 0 1.8935599962160683 0.13533449110186729 -1.0000010760366214 1;
	setAttr ".pm[11]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -9.5109235153967138 0.17376929722515433 2.1504337893989135e-15 1;
	setAttr ".pm[12]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -10.500223672082353 0.17376929722515433 2.3701025518424469e-15 1;
	setAttr ".pm[13]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -11.703780240227058 0.17376929722515433 2.6373457945210649e-15 1;
	setAttr ".pm[14]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -12.875926312066481 0.17376929722515433 2.8976145059570766e-15 1;
	setAttr ".pm[15]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -13.928707643645982 0.17376929722515508 3.1313789208000969e-15 1;
	setAttr ".pm[16]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -15.338164390135388 0.17376929722515508 3.444341187233257e-15 1;
	setAttr ".pm[17]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -17.042375757171094 0.17376929722515508 3.4443411872332574e-15 1;
	setAttr ".pm[18]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -0.64419300000000002 -13.5276 0.17376900000000314 1;
	setAttr ".pm[19]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -1.6150599999999999 -13.512600000000001 0.17376900000000314 1;
	setAttr ".pm[20]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -4.4291700000000001 -13.512600000000001 0.17376900000000312 1;
	setAttr ".pm[21]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -6.9456699999999998 -13.512600000000001 0.17376900000000314 1;
	setAttr ".pm[22]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -7.7752400000000002 -13.512600000000001 0.17376900000000312 1;
	setAttr ".pm[23]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -8.7057699999999993 -13.1126 0.17376900000000317 1;
	setAttr ".pm[24]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 0.64419300000000002 13.5276 -0.17376900000000289 1;
	setAttr ".pm[25]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 1.6150599999999999 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[26]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 4.4291700000000001 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[27]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503131e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -4.3510429945103838e-16 -17.197881028695463 -1.4403241938392897 1;
	setAttr ".pm[28]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 7.7752400000000002 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[29]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 8.7057699999999993 13.1126 -0.17376900000000289 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 0 0 0 1;
	setAttr -s 10 ".ma";
	setAttr -s 30 ".dpf[0:29]"  4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 
		4 4 4 4 4 4 4 4 4 4;
	setAttr -s 10 ".lw";
	setAttr ".mmi" yes;
	setAttr ".mi" 5;
	setAttr ".ucm" yes;
createNode tweak -n "tweak2";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000243F";
createNode objectSet -n "skinCluster2Set";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002440";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster2GroupId";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002441";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster2GroupParts";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002442";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode objectSet -n "tweakSet2";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002443";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId4";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002444";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts4";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002445";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode skinCluster -n "skinCluster3";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002446";
	setAttr -s 252 ".wl";
	setAttr ".wl[0].w[22]"  1;
	setAttr ".wl[1].w[22]"  1;
	setAttr -s 2 ".wl[2].w[21:22]"  0.8078431338071822 0.19215686619281769;
	setAttr -s 2 ".wl[3].w[21:22]"  0.22745096683502197 0.77254903316497803;
	setAttr -s 2 ".wl[4].w[21:22]"  0.23137253522872925 0.76862746477127075;
	setAttr ".wl[5].w[22]"  1;
	setAttr -s 2 ".wl[6].w[21:22]"  0.090196073055267334 0.90980392694473267;
	setAttr -s 2 ".wl[7].w[21:22]"  0.2235293984413147 0.7764706015586853;
	setAttr ".wl[8].w[22]"  1;
	setAttr -s 2 ".wl[9].w[21:22]"  0.19607841968536377 0.80392158031463612;
	setAttr ".wl[10].w[21]"  0.99999999999999989;
	setAttr ".wl[11].w[21]"  1;
	setAttr ".wl[12].w[21]"  1;
	setAttr ".wl[13].w[21]"  1;
	setAttr ".wl[14].w[21]"  0.99999999999999989;
	setAttr ".wl[15].w[21]"  1;
	setAttr ".wl[16].w[21]"  1;
	setAttr ".wl[17].w[21]"  1;
	setAttr ".wl[18].w[21]"  1;
	setAttr ".wl[19].w[21]"  1;
	setAttr ".wl[20].w[21]"  0.99999999999999989;
	setAttr ".wl[21].w[21]"  1;
	setAttr ".wl[22].w[21]"  0.99999999999999989;
	setAttr ".wl[23].w[21]"  0.99999999999999989;
	setAttr ".wl[24].w[21]"  1;
	setAttr ".wl[25].w[21]"  1;
	setAttr ".wl[26].w[21]"  1;
	setAttr ".wl[27].w[21]"  1;
	setAttr ".wl[28].w[21]"  0.99999999999999989;
	setAttr ".wl[29].w[21]"  1;
	setAttr ".wl[30].w[21]"  1;
	setAttr ".wl[31].w[21]"  1;
	setAttr -s 2 ".wl[32].w[20:21]"  0.55801779813568109 0.44198220186431886;
	setAttr -s 2 ".wl[33].w[20:21]"  0.079906371706247689 0.92009362829375252;
	setAttr -s 2 ".wl[34].w[20:21]"  0.1200351737155462 0.87996482628445372;
	setAttr -s 2 ".wl[35].w[20:21]"  0.18524016632385604 0.8147598336761438;
	setAttr -s 2 ".wl[36].w[20:21]"  0.066079411468264834 0.93392058853173521;
	setAttr -s 2 ".wl[37].w[20:21]"  0.094270530329221031 0.90572946967077883;
	setAttr -s 2 ".wl[38].w[20:21]"  0.22615352136908157 0.7738464786309186;
	setAttr -s 2 ".wl[39].w[20:21]"  0.00028035293854627476 0.99971964706145355;
	setAttr -s 2 ".wl[40].w[20:21]"  0.010997075115997176 0.98900292488400288;
	setAttr ".wl[41].w[21]"  0.99999999999999989;
	setAttr -s 2 ".wl[42].w[20:21]"  0.00035614553129511179 0.99964385446870496;
	setAttr -s 2 ".wl[43].w[20:21]"  0.0034506093349102301 0.99654939066508974;
	setAttr -s 2 ".wl[44].w[20:21]"  0.0022861720111900206 0.99771382798881003;
	setAttr ".wl[45].w[21]"  1;
	setAttr -s 2 ".wl[46].w[20:21]"  0.60218581171598595 0.39781418828401421;
	setAttr ".wl[47].w[21]"  1;
	setAttr -s 2 ".wl[48].w[20:21]"  0.00077422615333234859 0.99922577384666755;
	setAttr ".wl[49].w[21]"  1;
	setAttr ".wl[50].w[21]"  1;
	setAttr ".wl[51].w[21]"  1;
	setAttr ".wl[52].w[21]"  0.99999999999999989;
	setAttr ".wl[53].w[21]"  0.99999999999999989;
	setAttr -s 2 ".wl[54].w[20:21]"  0.014318879435707758 0.98568112056429247;
	setAttr -s 2 ".wl[55].w[20:21]"  0.7948659916723404 0.20513400832765963;
	setAttr -s 2 ".wl[56].w[20:21]"  0.7253808548246915 0.27461914517530867;
	setAttr -s 2 ".wl[57].w[20:21]"  0.6328245781007209 0.3671754218992791;
	setAttr -s 2 ".wl[58].w[20:21]"  0.52080878272241271 0.47919121727758729;
	setAttr -s 2 ".wl[59].w[20:21]"  0.083531161934466497 0.91646883806553348;
	setAttr -s 2 ".wl[60].w[20:21]"  0.16199444651309708 0.83800555348690287;
	setAttr -s 2 ".wl[61].w[20:21]"  0.5358232859974057 0.4641767140025943;
	setAttr -s 2 ".wl[62].w[20:21]"  0.47365313935444198 0.52634686064555802;
	setAttr ".wl[63].w[21]"  1;
	setAttr ".wl[64].w[21]"  1.0000000000000002;
	setAttr ".wl[65].w[21]"  1;
	setAttr ".wl[66].w[21]"  1;
	setAttr -s 2 ".wl[67].w[20:21]"  0.55480484567712629 0.44519515432287377;
	setAttr -s 2 ".wl[68].w[20:21]"  0.18181239056352463 0.81818760943647539;
	setAttr -s 2 ".wl[69].w[20:21]"  0.17260433036866007 0.82739566963134004;
	setAttr -s 2 ".wl[70].w[20:21]"  0.98841259042885266 0.011587409571147437;
	setAttr -s 3 ".wl[71].w[19:21]"  4.6028387100176185e-10 0.99994856631615148 5.1433223564502645e-05;
	setAttr -s 2 ".wl[72].w[20:21]"  0.91411986497196673 0.085880135028033266;
	setAttr -s 2 ".wl[73].w[20:21]"  0.99975063795331276 0.00024936204668711515;
	setAttr -s 2 ".wl[74].w[20:21]"  0.98605640474150369 0.013943595258496314;
	setAttr -s 2 ".wl[75].w[20:21]"  0.91798477841299997 0.082015221586999851;
	setAttr -s 2 ".wl[76].w[20:21]"  0.99658072910889628 0.003419270891103672;
	setAttr -s 2 ".wl[77].w[20:21]"  0.88071053636074836 0.11928946363925159;
	setAttr -s 2 ".wl[78].w[20:21]"  0.97549592771462834 0.024504072285371582;
	setAttr -s 2 ".wl[79].w[19:20]"  0.82514460732726236 0.17485539267273767;
	setAttr -s 2 ".wl[80].w[19:20]"  0.85691666553492851 0.14308333446507143;
	setAttr -s 2 ".wl[81].w[19:20]"  0.85530168389774963 0.14469831610225045;
	setAttr -s 2 ".wl[82].w[19:20]"  0.80083325164599695 0.19916674835400305;
	setAttr -s 2 ".wl[83].w[19:20]"  0.83195361235951215 0.1680463876404879;
	setAttr -s 2 ".wl[84].w[19:20]"  0.8160345196438975 0.18396548035610244;
	setAttr -s 2 ".wl[85].w[19:20]"  0.8409448104207613 0.1590551895792387;
	setAttr -s 2 ".wl[86].w[19:20]"  0.81028293006596031 0.18971706993403967;
	setAttr -s 2 ".wl[87].w[19:20]"  0.7928315227767998 0.20716847722320025;
	setAttr -s 2 ".wl[88].w[19:20]"  0.41810298582271271 0.58189701417728723;
	setAttr -s 2 ".wl[89].w[19:20]"  0.3996697818577627 0.6003302181422373;
	setAttr -s 2 ".wl[90].w[19:20]"  0.39428884722388691 0.6057111527761132;
	setAttr -s 2 ".wl[91].w[19:20]"  0.40556347643675594 0.59443652356324406;
	setAttr -s 2 ".wl[92].w[19:20]"  0.40076354829095856 0.5992364517090415;
	setAttr -s 2 ".wl[93].w[19:20]"  0.41900276993818919 0.58099723006181081;
	setAttr -s 2 ".wl[94].w[19:20]"  0.40065994540807037 0.59934005459192974;
	setAttr -s 2 ".wl[95].w[19:20]"  0.41529183265606584 0.58470816734393427;
	setAttr -s 2 ".wl[96].w[19:20]"  0.39421253161124375 0.60578746838875619;
	setAttr -s 2 ".wl[97].w[19:20]"  0.16214887276623668 0.83785112723376332;
	setAttr -s 2 ".wl[98].w[19:20]"  0.14188760849813253 0.85811239150186747;
	setAttr -s 2 ".wl[99].w[19:20]"  0.1340034247162577 0.8659965752837423;
	setAttr -s 2 ".wl[100].w[19:20]"  0.16934438569822266 0.83065561430177748;
	setAttr -s 2 ".wl[101].w[19:20]"  0.1518434143254748 0.84815658567452523;
	setAttr -s 2 ".wl[102].w[19:20]"  0.16415993704026427 0.83584006295973579;
	setAttr -s 2 ".wl[103].w[19:20]"  0.14103736065195596 0.85896263934804395;
	setAttr -s 2 ".wl[104].w[19:20]"  0.16743757999188208 0.83256242000811786;
	setAttr -s 2 ".wl[105].w[19:20]"  0.16696484682181742 0.83303515317818255;
	setAttr -s 3 ".wl[106].w";
	setAttr ".wl[106].w[13]" 0.080232509677349476;
	setAttr ".wl[106].w[18]" 0.0063684359012166685;
	setAttr ".wl[106].w[19]" 0.91339905442143388;
	setAttr -s 2 ".wl[107].w[18:19]"  0.0035622308502930937 0.99643776914970683;
	setAttr -s 3 ".wl[108].w";
	setAttr ".wl[108].w[13]" 0.32210260874315172;
	setAttr ".wl[108].w[18]" 9.9608708941758511e-06;
	setAttr ".wl[108].w[19]" 0.67788743038595412;
	setAttr -s 2 ".wl[109].w";
	setAttr ".wl[109].w[13]" 0.37654312179927457;
	setAttr ".wl[109].w[19]" 0.62345687820072548;
	setAttr -s 3 ".wl[110].w";
	setAttr ".wl[110].w[13]" 0.19530786674616479;
	setAttr ".wl[110].w[18]" 0.0016921708814029591;
	setAttr ".wl[110].w[19]" 0.80299996237243232;
	setAttr ".wl[111].w[19]"  1;
	setAttr ".wl[112].w[19]"  1;
	setAttr -s 2 ".wl[113].w";
	setAttr ".wl[113].w[13]" 0.02695917255580239;
	setAttr ".wl[113].w[19]" 0.97304082744419762;
	setAttr -s 2 ".wl[114].w";
	setAttr ".wl[114].w[13]" 0.23673776474557556;
	setAttr ".wl[114].w[19]" 0.76326223525442449;
	setAttr ".wl[115].w[22]"  1;
	setAttr ".wl[116].w[22]"  1;
	setAttr ".wl[117].w[22]"  1;
	setAttr ".wl[118].w[22]"  1;
	setAttr ".wl[119].w[22]"  1;
	setAttr ".wl[120].w[22]"  1;
	setAttr -s 2 ".wl[121].w[21:22]"  0.18823528289794919 0.81176471710205067;
	setAttr ".wl[122].w[22]"  1;
	setAttr ".wl[123].w[22]"  1;
	setAttr ".wl[124].w[22]"  1;
	setAttr -s 2 ".wl[125].w[20:21]"  1.6397157177714144e-06 0.99999836028428213;
	setAttr ".wl[126].w[28]"  1;
	setAttr -s 2 ".wl[127].w[27:28]"  0.74901959300041199 0.25098040699958801;
	setAttr -s 2 ".wl[128].w[27:28]"  0.2549019455909729 0.7450980544090271;
	setAttr -s 2 ".wl[129].w[27:28]"  0.27450978755950928 0.72549021244049072;
	setAttr -s 2 ".wl[130].w[27:28]"  0.57647058367729187 0.42352941632270819;
	setAttr -s 2 ".wl[131].w[27:28]"  0.52156862616539001 0.47843137383460999;
	setAttr -s 2 ".wl[132].w[27:28]"  0.30980390310287476 0.69019609689712524;
	setAttr -s 2 ".wl[133].w[27:28]"  0.52549019455909729 0.47450980544090271;
	setAttr -s 2 ".wl[134].w[27:28]"  0.32156860828399658 0.67843139171600342;
	setAttr ".wl[135].w[28]"  1;
	setAttr ".wl[136].w[27]"  0.99999999999999989;
	setAttr ".wl[137].w[27]"  1;
	setAttr ".wl[138].w[27]"  1;
	setAttr ".wl[139].w[27]"  1;
	setAttr ".wl[140].w[27]"  0.99999999999999989;
	setAttr ".wl[141].w[27]"  1;
	setAttr ".wl[142].w[27]"  0.99999999999999989;
	setAttr ".wl[143].w[27]"  1;
	setAttr ".wl[144].w[27]"  0.99999999999999989;
	setAttr ".wl[145].w[27]"  0.99999999999999989;
	setAttr ".wl[146].w[27]"  1;
	setAttr ".wl[147].w[27]"  1;
	setAttr ".wl[148].w[27]"  1;
	setAttr ".wl[149].w[27]"  1;
	setAttr ".wl[150].w[27]"  1;
	setAttr ".wl[151].w[27]"  1;
	setAttr ".wl[152].w[27]"  1;
	setAttr ".wl[153].w[27]"  1;
	setAttr ".wl[154].w[27]"  1;
	setAttr ".wl[155].w[27]"  1;
	setAttr ".wl[156].w[27]"  0.99999999999999989;
	setAttr ".wl[157].w[27]"  1;
	setAttr -s 2 ".wl[158].w[26:27]"  0.55802003182480198 0.44197996817519802;
	setAttr -s 2 ".wl[159].w[26:27]"  0.079906371706247689 0.92009362829375252;
	setAttr -s 2 ".wl[160].w[26:27]"  0.12003590968214792 0.87996409031785217;
	setAttr -s 2 ".wl[161].w[26:27]"  0.18524249077246041 0.81475750922753964;
	setAttr -s 2 ".wl[162].w[26:27]"  0.066079981518522651 0.93392001848147732;
	setAttr -s 2 ".wl[163].w[26:27]"  0.094270225961245596 0.90572977403875421;
	setAttr -s 2 ".wl[164].w[26:27]"  0.22615352136908157 0.7738464786309186;
	setAttr -s 2 ".wl[165].w[26:27]"  0.00028034401339881117 0.99971965598660117;
	setAttr -s 2 ".wl[166].w[26:27]"  0.010997075115997176 0.98900292488400288;
	setAttr ".wl[167].w[27]"  0.99999999999999989;
	setAttr -s 2 ".wl[168].w[26:27]"  0.00035614553129511179 0.99964385446870496;
	setAttr -s 2 ".wl[169].w[26:27]"  0.0034506083979491476 0.99654939160205092;
	setAttr -s 2 ".wl[170].w[26:27]"  0.0022861866296761779 0.99771381337032383;
	setAttr ".wl[171].w[27]"  1;
	setAttr -s 2 ".wl[172].w[26:27]"  0.60218581171598595 0.39781418828401416;
	setAttr ".wl[173].w[27]"  1;
	setAttr -s 2 ".wl[174].w[26:27]"  0.00077422615333234859 0.99922577384666755;
	setAttr ".wl[175].w[27]"  1;
	setAttr ".wl[176].w[27]"  1;
	setAttr ".wl[177].w[27]"  1;
	setAttr ".wl[178].w[27]"  1;
	setAttr ".wl[179].w[27]"  0.99999999999999989;
	setAttr -s 2 ".wl[180].w[26:27]"  0.014318879969235507 0.98568112003076469;
	setAttr -s 2 ".wl[181].w[26:27]"  0.7948659916723404 0.20513400832765963;
	setAttr -s 2 ".wl[182].w[26:27]"  0.72538017829296164 0.27461982170703836;
	setAttr -s 2 ".wl[183].w[26:27]"  0.63282514985195826 0.36717485014804174;
	setAttr -s 2 ".wl[184].w[26:27]"  0.52081032339715083 0.47918967660284911;
	setAttr -s 2 ".wl[185].w[26:27]"  0.083531824157251425 0.91646817584274853;
	setAttr -s 2 ".wl[186].w[26:27]"  0.16199564275685391 0.83800435724314604;
	setAttr -s 2 ".wl[187].w[26:27]"  0.53582167362248245 0.46417832637751755;
	setAttr -s 2 ".wl[188].w[26:27]"  0.47365251412542025 0.5263474858745798;
	setAttr ".wl[189].w[27]"  1;
	setAttr ".wl[190].w[27]"  1;
	setAttr ".wl[191].w[27]"  1;
	setAttr ".wl[192].w[27]"  1;
	setAttr -s 2 ".wl[193].w[26:27]"  0.55480445786410526 0.44519554213589474;
	setAttr -s 2 ".wl[194].w[26:27]"  0.18181238718334025 0.81818761281665964;
	setAttr -s 2 ".wl[195].w[26:27]"  0.17260270242137463 0.82739729757862546;
	setAttr -s 2 ".wl[196].w[26:27]"  0.98841259042885266 0.011587409571147437;
	setAttr -s 3 ".wl[197].w[25:27]"  4.6028776288391999e-10 0.99994856588125947 5.1433658452748225e-05;
	setAttr -s 2 ".wl[198].w[26:27]"  0.91412023823087907 0.085879761769120919;
	setAttr -s 2 ".wl[199].w[26:27]"  0.99975063802816577 0.00024936197183418943;
	setAttr -s 2 ".wl[200].w[26:27]"  0.98605640903052683 0.013943590969473047;
	setAttr -s 2 ".wl[201].w[26:27]"  0.91798477841299997 0.082015221586999851;
	setAttr -s 2 ".wl[202].w[26:27]"  0.99658071179597307 0.0034192882040270096;
	setAttr -s 2 ".wl[203].w[26:27]"  0.88071019444381804 0.11928980555618184;
	setAttr -s 2 ".wl[204].w[26:27]"  0.97549675642549405 0.024503243574506013;
	setAttr -s 2 ".wl[205].w[25:26]"  0.82514460732726236 0.17485539267273767;
	setAttr -s 2 ".wl[206].w[25:26]"  0.85691666311279024 0.14308333688720981;
	setAttr -s 2 ".wl[207].w[25:26]"  0.85530169421742852 0.14469830578257151;
	setAttr -s 2 ".wl[208].w[25:26]"  0.80083325090005775 0.19916674909994236;
	setAttr -s 2 ".wl[209].w[25:26]"  0.83195361235951215 0.1680463876404879;
	setAttr -s 2 ".wl[210].w[25:26]"  0.8160346227272226 0.1839653772727774;
	setAttr -s 2 ".wl[211].w[25:26]"  0.84094430821315647 0.15905569178684353;
	setAttr -s 2 ".wl[212].w[25:26]"  0.81028287732227922 0.18971712267772081;
	setAttr -s 2 ".wl[213].w[25:26]"  0.79283200153461508 0.20716799846538497;
	setAttr -s 2 ".wl[214].w[25:26]"  0.41810298582271282 0.58189701417728723;
	setAttr -s 2 ".wl[215].w[25:26]"  0.39966886607930546 0.60033113392069448;
	setAttr -s 2 ".wl[216].w[25:26]"  0.39428880860595811 0.60571119139404206;
	setAttr -s 2 ".wl[217].w[25:26]"  0.40556286399387398 0.59443713600612602;
	setAttr -s 2 ".wl[218].w[25:26]"  0.40076353618424848 0.59923646381575169;
	setAttr -s 2 ".wl[219].w[25:26]"  0.41900276993818919 0.58099723006181081;
	setAttr -s 2 ".wl[220].w[25:26]"  0.40065994261041055 0.5993400573895894;
	setAttr -s 2 ".wl[221].w[25:26]"  0.4152912194667443 0.58470878053325559;
	setAttr -s 2 ".wl[222].w[25:26]"  0.39421313389077128 0.60578686610922883;
	setAttr -s 2 ".wl[223].w[25:26]"  0.16214895125428189 0.83785104874571803;
	setAttr -s 2 ".wl[224].w[25:26]"  0.1418873025175777 0.85811269748242225;
	setAttr -s 2 ".wl[225].w[25:26]"  0.13400310769960763 0.86599689230039234;
	setAttr -s 2 ".wl[226].w[25:26]"  0.1693440570773137 0.83065594292268641;
	setAttr -s 2 ".wl[227].w[25:26]"  0.15184371761478888 0.84815628238521124;
	setAttr -s 2 ".wl[228].w[25:26]"  0.16415960847048763 0.83584039152951228;
	setAttr -s 2 ".wl[229].w[25:26]"  0.14103703742934112 0.85896296257065874;
	setAttr -s 2 ".wl[230].w[25:26]"  0.16743757712648522 0.83256242287351467;
	setAttr -s 2 ".wl[231].w[25:26]"  0.16696487107097727 0.83303512892902254;
	setAttr -s 3 ".wl[232].w";
	setAttr ".wl[232].w[13]" 0.08023265698117249;
	setAttr ".wl[232].w[24]" 0.0063684492976847232;
	setAttr ".wl[232].w[25]" 0.9133988937211428;
	setAttr -s 2 ".wl[233].w[24:25]"  0.0035622308502930937 0.99643776914970683;
	setAttr -s 3 ".wl[234].w";
	setAttr ".wl[234].w[13]" 0.32210260975003985;
	setAttr ".wl[234].w[24]" 9.9608794540000059e-06;
	setAttr ".wl[234].w[25]" 0.67788742937050617;
	setAttr -s 2 ".wl[235].w";
	setAttr ".wl[235].w[13]" 0.37654277500295863;
	setAttr ".wl[235].w[25]" 0.62345722499704137;
	setAttr -s 3 ".wl[236].w";
	setAttr ".wl[236].w[13]" 0.19530786674616477;
	setAttr ".wl[236].w[24]" 0.0016921708814029591;
	setAttr ".wl[236].w[25]" 0.80299996237243243;
	setAttr ".wl[237].w[25]"  1;
	setAttr ".wl[238].w[25]"  1;
	setAttr -s 2 ".wl[239].w";
	setAttr ".wl[239].w[13]" 0.02695917255580239;
	setAttr ".wl[239].w[25]" 0.97304082744419762;
	setAttr -s 2 ".wl[240].w";
	setAttr ".wl[240].w[13]" 0.23673776474557556;
	setAttr ".wl[240].w[25]" 0.76326223525442449;
	setAttr ".wl[241].w[28]"  1;
	setAttr ".wl[242].w[28]"  1;
	setAttr -s 2 ".wl[243].w[27:28]"  0.0078431367874145508 0.99215686321258545;
	setAttr ".wl[244].w[28]"  1;
	setAttr ".wl[245].w[28]"  1;
	setAttr -s 2 ".wl[246].w[27:28]"  0.058823525905609131 0.94117647409439087;
	setAttr ".wl[247].w[28]"  1;
	setAttr ".wl[248].w[28]"  1;
	setAttr ".wl[249].w[28]"  1;
	setAttr ".wl[250].w[28]"  1;
	setAttr -s 2 ".wl[251].w[26:27]"  1.6397157177714144e-06 0.99999836028428224;
	setAttr -s 30 ".pm";
	setAttr ".pm[0]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -8.9231745720989668 0.17376929722515433 2.0199273074892598e-15 1;
	setAttr ".pm[1]" -type "matrix" -3.4450928483976665e-16 -2.2204460492503131e-16 -1 0 -1 4.9303806576313238e-32 3.4450928483976665e-16 0
		 -7.6496428045251064e-32 1 -2.2204460492503131e-16 0 8.9231745720989668 0.17376929722515455 0.999999999999997 1;
	setAttr ".pm[2]" -type "matrix" -3.4450928483976665e-16 -2.2204460492503131e-16 -1 0 -1 4.9303806576313238e-32 3.4450928483976665e-16 0
		 -7.6496428045251064e-32 1 -2.2204460492503131e-16 0 4.6515061293712359 0.17376929722515452 0.99999999999999889 1;
	setAttr ".pm[3]" -type "matrix" 5.8331365260285766e-07 -3.4717393473770988e-07 -0.99999999999976963 0 -0.4794097213532717 0.87759120270866275 -5.8432302659159539e-07 0
		 0.87759120270866331 0.47940972135350218 3.454723706304003e-07 0 0.53189973592848949 -0.61121325699033013 1.0000005224619188 1;
	setAttr ".pm[4]" -type "matrix" -3.7839275046629232e-09 -4.9514660478913824e-07 -0.99999999999987765 0 4.5717040610908244e-16 0.99999999999987776 -4.9514660478913814e-07 0
		 1.0000000000000002 -2.2981828101998501e-15 -3.7839275046623533e-09 0 -1.0271901970466448 -0.13533431203966553 1.0000008717993354 1;
	setAttr ".pm[5]" -type "matrix" -3.7839275046629232e-09 -4.9514660478913824e-07 -0.99999999999987765 0 4.5717040610908244e-16 0.99999999999987776 -4.9514660478913814e-07 0
		 1.0000000000000002 -2.2981828101998501e-15 -3.7839275046623533e-09 0 -1.8935622781747257 -0.1353343120396657 1.0000008717993347 1;
	setAttr ".pm[6]" -type "matrix" 2.2204460492503131e-16 9.9579925010295987e-17 -1 0 1 -2.2111185107375414e-32 2.2204460492503131e-16 0
		 4.9303806576313238e-32 -1 -9.9579925010295987e-17 0 -8.9231700000000007 -0.1737689999999999 -1.000000000000002 1;
	setAttr ".pm[7]" -type "matrix" 2.2204460492503131e-16 9.9579925010295987e-17 -1 0 1 -2.2111185107375414e-32 2.2204460492503131e-16 0
		 4.9303806576313238e-32 -1 -9.9579925010295987e-17 0 -4.65151 -0.1737689999999999 -1.0000000000000011 1;
	setAttr ".pm[8]" -type "matrix" 5.8331365260285766e-07 -3.4602377056398311e-07 -0.99999999999976996 0 0.47940972135327098 -0.87759120270866364 5.8331365263106153e-07 0
		 -0.87759120270866364 -0.47940972135350091 -3.460237705164382e-07 0 -0.53189953941047974 0.61121351838277305 -1.0000005217588994 1;
	setAttr ".pm[9]" -type "matrix" -3.7839275046628231e-09 -5.0889760207317231e-07 -0.99999999999987077 0 -5.094072503275622e-16 -0.99999999999987077 5.0889760207317231e-07 0
		 -1 2.5476401720380396e-15 3.7839275046620083e-09 0 1.0271899962160689 0.13533449110186921 -1.0000010727583399 1;
	setAttr ".pm[10]" -type "matrix" -3.7839275046628231e-09 -5.0889760207317231e-07 -0.99999999999987077 0 -5.094072503275622e-16 -0.99999999999987077 5.0889760207317231e-07 0
		 -1 2.5476401720380396e-15 3.7839275046620083e-09 0 1.8935599962160683 0.13533449110186729 -1.0000010760366214 1;
	setAttr ".pm[11]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -9.5109235153967138 0.17376929722515433 2.1504337893989135e-15 1;
	setAttr ".pm[12]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -10.500223672082353 0.17376929722515433 2.3701025518424469e-15 1;
	setAttr ".pm[13]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -11.703780240227058 0.17376929722515433 2.6373457945210649e-15 1;
	setAttr ".pm[14]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -12.875926312066481 0.17376929722515433 2.8976145059570766e-15 1;
	setAttr ".pm[15]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -13.928707643645982 0.17376929722515508 3.1313789208000969e-15 1;
	setAttr ".pm[16]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -15.338164390135388 0.17376929722515508 3.444341187233257e-15 1;
	setAttr ".pm[17]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -17.042375757171094 0.17376929722515508 3.4443411872332574e-15 1;
	setAttr ".pm[18]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -0.64419300000000002 -13.5276 0.17376900000000314 1;
	setAttr ".pm[19]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -1.6150599999999999 -13.512600000000001 0.17376900000000314 1;
	setAttr ".pm[20]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -4.4291700000000001 -13.512600000000001 0.17376900000000312 1;
	setAttr ".pm[21]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -6.9456699999999998 -13.512600000000001 0.17376900000000314 1;
	setAttr ".pm[22]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -7.7752400000000002 -13.512600000000001 0.17376900000000312 1;
	setAttr ".pm[23]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -8.7057699999999993 -13.1126 0.17376900000000317 1;
	setAttr ".pm[24]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 0.64419300000000002 13.5276 -0.17376900000000289 1;
	setAttr ".pm[25]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 1.6150599999999999 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[26]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 4.4291700000000001 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[27]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 6.9456699999999998 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[28]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 7.7752400000000002 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[29]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 8.7057699999999993 13.1126 -0.17376900000000289 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 0 0 0 1;
	setAttr -s 15 ".ma";
	setAttr -s 30 ".dpf[0:29]"  4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 
		4 4 4 4 4 4 4 4 4 4;
	setAttr -s 15 ".lw";
	setAttr ".mmi" yes;
	setAttr ".mi" 5;
	setAttr ".ucm" yes;
createNode tweak -n "tweak3";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002447";
createNode objectSet -n "skinCluster3Set";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002448";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster3GroupId";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002449";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster3GroupParts";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000244A";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode objectSet -n "tweakSet3";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000244B";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId6";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000244C";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts6";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000244D";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode skinCluster -n "skinCluster4";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000244E";
	setAttr -s 160 ".wl";
	setAttr -s 5 ".wl[0].w";
	setAttr ".wl[0].w[0]" 0.092016084765894388;
	setAttr ".wl[0].w[1]" 0.052535984074895223;
	setAttr ".wl[0].w[6]" 0.051449884150989431;
	setAttr ".wl[0].w[11]" 0.7569727993738542;
	setAttr ".wl[0].w[12]" 0.047025247634366843;
	setAttr -s 4 ".wl[1].w";
	setAttr ".wl[1].w[0]" 0.30013080535211606;
	setAttr ".wl[1].w[1]" 0.34353813189467464;
	setAttr ".wl[1].w[6]" 0.34114714332419549;
	setAttr ".wl[1].w[11]" 0.015183919429013776;
	setAttr -s 3 ".wl[2].w";
	setAttr ".wl[2].w[0]" 0.2429987704690369;
	setAttr ".wl[2].w[1]" 0.37850092253591194;
	setAttr ".wl[2].w[6]" 0.37850030699505122;
	setAttr -s 3 ".wl[3].w";
	setAttr ".wl[3].w[0]" 0.4656607709149454;
	setAttr ".wl[3].w[1]" 0.16668008660937433;
	setAttr ".wl[3].w[6]" 0.36765914247568032;
	setAttr -s 4 ".wl[4].w";
	setAttr ".wl[4].w[0]" 0.44241215197817674;
	setAttr ".wl[4].w[1]" 0.077464211373429265;
	setAttr ".wl[4].w[6]" 0.015170576462170602;
	setAttr ".wl[4].w[11]" 0.46495306018622329;
	setAttr -s 3 ".wl[5].w";
	setAttr ".wl[5].w[0]" 0.33237291685330628;
	setAttr ".wl[5].w[1]" 0.33205019426785254;
	setAttr ".wl[5].w[11]" 0.33557688887884118;
	setAttr -s 3 ".wl[6].w";
	setAttr ".wl[6].w[0]" 0.10552560880220276;
	setAttr ".wl[6].w[1]" 0.88420051601548111;
	setAttr ".wl[6].w[11]" 0.010273875182316136;
	setAttr -s 3 ".wl[7].w";
	setAttr ".wl[7].w[0]" 0.011464779827911713;
	setAttr ".wl[7].w[1]" 0.98780282927365859;
	setAttr ".wl[7].w[11]" 0.00073239089842980166;
	setAttr -s 3 ".wl[8].w";
	setAttr ".wl[8].w[0]" 0.35983028165982134;
	setAttr ".wl[8].w[1]" 0.35981267416403045;
	setAttr ".wl[8].w[11]" 0.28035704417614826;
	setAttr -s 3 ".wl[9].w";
	setAttr ".wl[9].w[0]" 0.35013620418492569;
	setAttr ".wl[9].w[1]" 0.35001883630504094;
	setAttr ".wl[9].w[11]" 0.29984495951003332;
	setAttr -s 2 ".wl[10].w[0:1]"  0.23158909160014307 0.76841090839985693;
	setAttr -s 3 ".wl[11].w";
	setAttr ".wl[11].w[0]" 0.3778102063757201;
	setAttr ".wl[11].w[1]" 0.36178906957581231;
	setAttr ".wl[11].w[11]" 0.26040072404846754;
	setAttr -s 3 ".wl[12].w";
	setAttr ".wl[12].w[0]" 0.38181583025087423;
	setAttr ".wl[12].w[1]" 0.24503295932369579;
	setAttr ".wl[12].w[11]" 0.37315121042542998;
	setAttr -s 3 ".wl[13].w";
	setAttr ".wl[13].w[0]" 0.3697219397926898;
	setAttr ".wl[13].w[1]" 0.36835236966127682;
	setAttr ".wl[13].w[11]" 0.26192569054603337;
	setAttr ".wl[14].w[1]"  0.99999999999999989;
	setAttr ".wl[15].w[1]"  1;
	setAttr ".wl[16].w[1]"  1;
	setAttr ".wl[17].w[1]"  0.99999999999999989;
	setAttr ".wl[18].w[1]"  1;
	setAttr ".wl[19].w[1]"  0.99999999999999989;
	setAttr ".wl[20].w[1]"  1.0000000000000002;
	setAttr ".wl[21].w[1]"  1;
	setAttr -s 4 ".wl[22].w";
	setAttr ".wl[22].w[0]" 0.14443859085699395;
	setAttr ".wl[22].w[1]" 0.12619036794139254;
	setAttr ".wl[22].w[11]" 0.72151792918508251;
	setAttr ".wl[22].w[12]" 0.0078531120165307323;
	setAttr -s 3 ".wl[23].w";
	setAttr ".wl[23].w[0]" 0.073750987023199766;
	setAttr ".wl[23].w[1]" 0.91809738742537883;
	setAttr ".wl[23].w[11]" 0.0081516255514213591;
	setAttr -s 3 ".wl[24].w";
	setAttr ".wl[24].w[0]" 0.12695207257113633;
	setAttr ".wl[24].w[1]" 0.86589357588397253;
	setAttr ".wl[24].w[11]" 0.007154351544891315;
	setAttr -s 2 ".wl[25].w[0:1]"  0.38236563001161872 0.61763436998838117;
	setAttr -s 2 ".wl[26].w[0:1]"  0.31702035843302445 0.68297964156697555;
	setAttr -s 2 ".wl[27].w[0:1]"  0.26501112977554769 0.73498887022445236;
	setAttr ".wl[28].w[1]"  1;
	setAttr -s 3 ".wl[29].w";
	setAttr ".wl[29].w[0]" 0.058584289109894105;
	setAttr ".wl[29].w[1]" 0.9327356142718034;
	setAttr ".wl[29].w[11]" 0.0086800966183024596;
	setAttr -s 3 ".wl[30].w";
	setAttr ".wl[30].w[0]" 0.23185862713901936;
	setAttr ".wl[30].w[1]" 0.22873037020617937;
	setAttr ".wl[30].w[11]" 0.53941100265480124;
	setAttr -s 4 ".wl[31].w";
	setAttr ".wl[31].w[0]" 0.60782378735308995;
	setAttr ".wl[31].w[1]" 0.15083510820467133;
	setAttr ".wl[31].w[6]" 0.058221600682937601;
	setAttr ".wl[31].w[11]" 0.18311950375930111;
	setAttr -s 4 ".wl[32].w";
	setAttr ".wl[32].w[0]" 0.3439442906243948;
	setAttr ".wl[32].w[1]" 0.27121150860288529;
	setAttr ".wl[32].w[6]" 0.27121135638492577;
	setAttr ".wl[32].w[11]" 0.11363284438779414;
	setAttr -s 3 ".wl[33].w";
	setAttr ".wl[33].w[0]" 0.31189675294573321;
	setAttr ".wl[33].w[1]" 0.60831988673721926;
	setAttr ".wl[33].w[11]" 0.079783360317047441;
	setAttr -s 3 ".wl[34].w";
	setAttr ".wl[34].w[0]" 0.17440384631345596;
	setAttr ".wl[34].w[1]" 0.79723991262072524;
	setAttr ".wl[34].w[11]" 0.028356241065818917;
	setAttr -s 3 ".wl[35].w";
	setAttr ".wl[35].w[0]" 0.19079980184523784;
	setAttr ".wl[35].w[1]" 0.78786208043501516;
	setAttr ".wl[35].w[11]" 0.021338117719746891;
	setAttr -s 3 ".wl[36].w";
	setAttr ".wl[36].w[0]" 0.31157003871757155;
	setAttr ".wl[36].w[1]" 0.65922111003894035;
	setAttr ".wl[36].w[11]" 0.029208851243488199;
	setAttr -s 3 ".wl[37].w";
	setAttr ".wl[37].w[0]" 0.39954485714697585;
	setAttr ".wl[37].w[1]" 0.55116912742062119;
	setAttr ".wl[37].w[11]" 0.049286015432402935;
	setAttr -s 3 ".wl[38].w";
	setAttr ".wl[38].w[0]" 0.43573164464763303;
	setAttr ".wl[38].w[1]" 0.47722583111297778;
	setAttr ".wl[38].w[11]" 0.087042524239389379;
	setAttr -s 3 ".wl[39].w";
	setAttr ".wl[39].w[0]" 0.45691285174932494;
	setAttr ".wl[39].w[1]" 0.45959149979464198;
	setAttr ".wl[39].w[11]" 0.083495648456033092;
	setAttr -s 3 ".wl[40].w";
	setAttr ".wl[40].w[0]" 0.50940792238657728;
	setAttr ".wl[40].w[1]" 0.33679576970435038;
	setAttr ".wl[40].w[11]" 0.15379630790907223;
	setAttr ".wl[41].w[1]"  1;
	setAttr -s 3 ".wl[42].w";
	setAttr ".wl[42].w[0]" 0.0048162387106581708;
	setAttr ".wl[42].w[1]" 0.99515708411743387;
	setAttr ".wl[42].w[11]" 2.667717190794435e-05;
	setAttr -s 4 ".wl[43].w";
	setAttr ".wl[43].w[0]" 0.01962011422627245;
	setAttr ".wl[43].w[1]" 0.97779683750559099;
	setAttr ".wl[43].w[6]" 0.0025173719176386439;
	setAttr ".wl[43].w[11]" 6.5676350497941244e-05;
	setAttr -s 2 ".wl[44].w[1:2]"  0.15632148459553721 0.84367851540446293;
	setAttr -s 2 ".wl[45].w[1:2]"  0.14434736797535741 0.85565263202464259;
	setAttr -s 2 ".wl[46].w[1:2]"  0.11469336526850292 0.88530663473149707;
	setAttr -s 2 ".wl[47].w[1:2]"  0.085210642681171109 0.91478935731882882;
	setAttr -s 2 ".wl[48].w[1:2]"  0.099542634561657906 0.90045736543834209;
	setAttr -s 2 ".wl[49].w[1:2]"  0.083326042079011078 0.91667395792098894;
	setAttr -s 2 ".wl[50].w[1:2]"  0.094992753118276596 0.9050072468817234;
	setAttr -s 2 ".wl[51].w[1:2]"  0.11124914006721208 0.8887508599327878;
	setAttr -s 2 ".wl[52].w[1:2]"  0.12121701568855996 0.87878298431143997;
	setAttr -s 2 ".wl[53].w[1:2]"  0.10057248483547862 0.89942751516452146;
	setAttr -s 2 ".wl[54].w[1:2]"  0.72299709455966821 0.27700290544033179;
	setAttr -s 2 ".wl[55].w[1:2]"  0.5463975460203303 0.45360245397966975;
	setAttr -s 2 ".wl[56].w[1:2]"  0.61231025551845719 0.3876897444815427;
	setAttr -s 2 ".wl[57].w[1:2]"  0.61839123070240021 0.38160876929759974;
	setAttr -s 2 ".wl[58].w[1:2]"  0.58831307291984558 0.41168692708015442;
	setAttr -s 2 ".wl[59].w[1:2]"  0.55586860371116831 0.44413139628883169;
	setAttr -s 2 ".wl[60].w[1:2]"  0.67783632963687623 0.32216367036312366;
	setAttr -s 2 ".wl[61].w[1:2]"  0.52487850839588268 0.47512149160411726;
	setAttr -s 2 ".wl[62].w[1:2]"  0.65334352043903376 0.34665647956096629;
	setAttr -s 2 ".wl[63].w[1:2]"  0.74932820912822784 0.2506717908717721;
	setAttr -s 2 ".wl[64].w[1:2]"  0.95948231981589471 0.040517680184105322;
	setAttr -s 2 ".wl[65].w[1:2]"  0.91245535137976452 0.087544648620235629;
	setAttr -s 2 ".wl[66].w[1:2]"  0.94647835429762173 0.053521645702378128;
	setAttr -s 2 ".wl[67].w[1:2]"  0.96269768290221691 0.037302317097783089;
	setAttr -s 2 ".wl[68].w[1:2]"  0.95928629411248389 0.040713705887516029;
	setAttr -s 2 ".wl[69].w[1:2]"  0.92227574810385693 0.07772425189614296;
	setAttr -s 2 ".wl[70].w[1:2]"  0.91092000428409725 0.089079995715902555;
	setAttr -s 2 ".wl[71].w[1:2]"  0.89677677723044491 0.10322322276955492;
	setAttr -s 2 ".wl[72].w[1:2]"  0.94327751695823581 0.056722483041764145;
	setAttr -s 2 ".wl[73].w[1:2]"  0.89238834691144131 0.10761165308855872;
	setAttr ".wl[74].w[2]"  1;
	setAttr ".wl[75].w[2]"  1;
	setAttr ".wl[76].w[2]"  1;
	setAttr ".wl[77].w[2]"  1;
	setAttr ".wl[78].w[2]"  1;
	setAttr ".wl[79].w[2]"  1;
	setAttr ".wl[80].w[2]"  1;
	setAttr ".wl[81].w[2]"  1;
	setAttr ".wl[82].w[2]"  1;
	setAttr ".wl[83].w[2]"  1;
	setAttr -s 3 ".wl[84].w";
	setAttr ".wl[84].w[0]" 0.33237351889329869;
	setAttr ".wl[84].w[6]" 0.33205079735360948;
	setAttr ".wl[84].w[11]" 0.33557568375309188;
	setAttr -s 3 ".wl[85].w";
	setAttr ".wl[85].w[0]" 0.10552559679886304;
	setAttr ".wl[85].w[6]" 0.88420052861204446;
	setAttr ".wl[85].w[11]" 0.010273874589092413;
	setAttr -s 3 ".wl[86].w";
	setAttr ".wl[86].w[0]" 0.0114647764176005;
	setAttr ".wl[86].w[6]" 0.98780283258937629;
	setAttr ".wl[86].w[11]" 0.00073239099302336078;
	setAttr -s 3 ".wl[87].w";
	setAttr ".wl[87].w[0]" 0.35983027655189559;
	setAttr ".wl[87].w[6]" 0.35981266905444165;
	setAttr ".wl[87].w[11]" 0.28035705439366276;
	setAttr -s 3 ".wl[88].w";
	setAttr ".wl[88].w[0]" 0.35013657447375984;
	setAttr ".wl[88].w[6]" 0.35001920747635074;
	setAttr ".wl[88].w[11]" 0.29984421804988937;
	setAttr -s 2 ".wl[89].w";
	setAttr ".wl[89].w[0]" 0.23158909160014307;
	setAttr ".wl[89].w[6]" 0.76841090839985693;
	setAttr -s 3 ".wl[90].w";
	setAttr ".wl[90].w[0]" 0.3778102063757201;
	setAttr ".wl[90].w[6]" 0.36178906957581231;
	setAttr ".wl[90].w[11]" 0.26040072404846754;
	setAttr -s 3 ".wl[91].w";
	setAttr ".wl[91].w[0]" 0.38181583025087423;
	setAttr ".wl[91].w[6]" 0.24503295932369579;
	setAttr ".wl[91].w[11]" 0.37315121042542998;
	setAttr -s 3 ".wl[92].w";
	setAttr ".wl[92].w[0]" 0.36972193979268975;
	setAttr ".wl[92].w[6]" 0.36835236966127682;
	setAttr ".wl[92].w[11]" 0.26192569054603332;
	setAttr ".wl[93].w[6]"  0.99999999999999989;
	setAttr ".wl[94].w[6]"  1;
	setAttr ".wl[95].w[6]"  1;
	setAttr ".wl[96].w[6]"  1;
	setAttr ".wl[97].w[6]"  1;
	setAttr ".wl[98].w[6]"  1;
	setAttr ".wl[99].w[6]"  1;
	setAttr ".wl[100].w[6]"  1;
	setAttr -s 4 ".wl[101].w";
	setAttr ".wl[101].w[0]" 0.14443857515665098;
	setAttr ".wl[101].w[6]" 0.12619035125590841;
	setAttr ".wl[101].w[11]" 0.72151795843417987;
	setAttr ".wl[101].w[12]" 0.0078531151532607382;
	setAttr -s 3 ".wl[102].w";
	setAttr ".wl[102].w[0]" 0.073750986737694452;
	setAttr ".wl[102].w[6]" 0.91809738804799956;
	setAttr ".wl[102].w[11]" 0.0081516252143059523;
	setAttr -s 3 ".wl[103].w";
	setAttr ".wl[103].w[0]" 0.12695207257113633;
	setAttr ".wl[103].w[6]" 0.86589357588397253;
	setAttr ".wl[103].w[11]" 0.007154351544891315;
	setAttr -s 2 ".wl[104].w";
	setAttr ".wl[104].w[0]" 0.38236563001161872;
	setAttr ".wl[104].w[6]" 0.61763436998838117;
	setAttr -s 2 ".wl[105].w";
	setAttr ".wl[105].w[0]" 0.31702035843302445;
	setAttr ".wl[105].w[6]" 0.68297964156697555;
	setAttr -s 2 ".wl[106].w";
	setAttr ".wl[106].w[0]" 0.26501112977554769;
	setAttr ".wl[106].w[6]" 0.73498887022445236;
	setAttr ".wl[107].w[6]"  1;
	setAttr -s 3 ".wl[108].w";
	setAttr ".wl[108].w[0]" 0.058584289109894105;
	setAttr ".wl[108].w[6]" 0.9327356142718034;
	setAttr ".wl[108].w[11]" 0.0086800966183024596;
	setAttr -s 3 ".wl[109].w";
	setAttr ".wl[109].w[0]" 0.23185806735310135;
	setAttr ".wl[109].w[6]" 0.22872982224682128;
	setAttr ".wl[109].w[11]" 0.5394121104000773;
	setAttr -s 3 ".wl[110].w";
	setAttr ".wl[110].w[0]" 0.31189638590180263;
	setAttr ".wl[110].w[6]" 0.60832047451602322;
	setAttr ".wl[110].w[11]" 0.079783139582174215;
	setAttr -s 3 ".wl[111].w";
	setAttr ".wl[111].w[0]" 0.17440384631345593;
	setAttr ".wl[111].w[6]" 0.79723991262072513;
	setAttr ".wl[111].w[11]" 0.028356241065818914;
	setAttr -s 3 ".wl[112].w";
	setAttr ".wl[112].w[0]" 0.19079980002897456;
	setAttr ".wl[112].w[6]" 0.78786208169973548;
	setAttr ".wl[112].w[11]" 0.021338118271289917;
	setAttr -s 3 ".wl[113].w";
	setAttr ".wl[113].w[0]" 0.31157003871757155;
	setAttr ".wl[113].w[6]" 0.65922111003894035;
	setAttr ".wl[113].w[11]" 0.029208851243488203;
	setAttr -s 3 ".wl[114].w";
	setAttr ".wl[114].w[0]" 0.39954485714697585;
	setAttr ".wl[114].w[6]" 0.55116912742062119;
	setAttr ".wl[114].w[11]" 0.049286015432402935;
	setAttr -s 3 ".wl[115].w";
	setAttr ".wl[115].w[0]" 0.43573178401639717;
	setAttr ".wl[115].w[6]" 0.47722615358922998;
	setAttr ".wl[115].w[11]" 0.087042062394372857;
	setAttr -s 3 ".wl[116].w";
	setAttr ".wl[116].w[0]" 0.45691285174932494;
	setAttr ".wl[116].w[6]" 0.45959149979464198;
	setAttr ".wl[116].w[11]" 0.083495648456033092;
	setAttr -s 3 ".wl[117].w";
	setAttr ".wl[117].w[0]" 0.50940792238657728;
	setAttr ".wl[117].w[6]" 0.33679576970435038;
	setAttr ".wl[117].w[11]" 0.15379630790907223;
	setAttr ".wl[118].w[6]"  1;
	setAttr -s 3 ".wl[119].w";
	setAttr ".wl[119].w[0]" 0.004816239218935865;
	setAttr ".wl[119].w[6]" 0.99515708360737676;
	setAttr ".wl[119].w[11]" 2.6677173687362268e-05;
	setAttr -s 2 ".wl[120].w[6:7]"  0.15632148832082748 0.84367851167917252;
	setAttr -s 2 ".wl[121].w[6:7]"  0.14434737114384039 0.85565262885615967;
	setAttr -s 2 ".wl[122].w[6:7]"  0.11469319127929464 0.88530680872070544;
	setAttr -s 2 ".wl[123].w[6:7]"  0.085210651769953905 0.91478934823004587;
	setAttr -s 2 ".wl[124].w[6:7]"  0.099542632699012756 0.90045736730098724;
	setAttr -s 2 ".wl[125].w[6:7]"  0.083326042893496446 0.91667395710650368;
	setAttr -s 2 ".wl[126].w[6:7]"  0.094992753118276596 0.9050072468817234;
	setAttr -s 2 ".wl[127].w[6:7]"  0.11124914006721208 0.8887508599327878;
	setAttr -s 2 ".wl[128].w[6:7]"  0.12121701345700936 0.8787829865429907;
	setAttr -s 2 ".wl[129].w[6:7]"  0.1005724875365382 0.89942751246346186;
	setAttr -s 2 ".wl[130].w[6:7]"  0.72299709019913572 0.27700290980086451;
	setAttr -s 2 ".wl[131].w[6:7]"  0.54639755765031361 0.45360244234968639;
	setAttr -s 2 ".wl[132].w[6:7]"  0.61231025551845719 0.3876897444815427;
	setAttr -s 2 ".wl[133].w[6:7]"  0.61839123070240021 0.38160876929759974;
	setAttr -s 2 ".wl[134].w[6:7]"  0.58831307850778103 0.41168692149221897;
	setAttr -s 2 ".wl[135].w[6:7]"  0.55586860371116831 0.44413139628883169;
	setAttr -s 2 ".wl[136].w[6:7]"  0.67783632963687623 0.32216367036312366;
	setAttr -s 2 ".wl[137].w[6:7]"  0.52487907688324431 0.4751209231167558;
	setAttr -s 2 ".wl[138].w[6:7]"  0.6533435195376901 0.34665648046230979;
	setAttr -s 2 ".wl[139].w[6:7]"  0.74932820912822784 0.2506717908717721;
	setAttr -s 2 ".wl[140].w[6:7]"  0.95948231981589471 0.040517680184105322;
	setAttr -s 2 ".wl[141].w[6:7]"  0.91245535595591964 0.087544644044080383;
	setAttr -s 2 ".wl[142].w[6:7]"  0.9464783551609478 0.053521644839052099;
	setAttr -s 2 ".wl[143].w[6:7]"  0.96269768476486206 0.037302315235137939;
	setAttr -s 2 ".wl[144].w[6:7]"  0.95928629411248389 0.040713705887516029;
	setAttr -s 2 ".wl[145].w[6:7]"  0.92227574810385693 0.07772425189614296;
	setAttr -s 2 ".wl[146].w[6:7]"  0.91092000452854005 0.089079995471460116;
	setAttr -s 2 ".wl[147].w[6:7]"  0.89677695429765347 0.1032230457023466;
	setAttr -s 2 ".wl[148].w[6:7]"  0.94327751695823581 0.056722483041764145;
	setAttr -s 2 ".wl[149].w[6:7]"  0.89238834691144131 0.10761165308855876;
	setAttr ".wl[150].w[7]"  1;
	setAttr ".wl[151].w[7]"  1;
	setAttr ".wl[152].w[7]"  1;
	setAttr ".wl[153].w[7]"  1;
	setAttr ".wl[154].w[7]"  1;
	setAttr ".wl[155].w[7]"  1;
	setAttr ".wl[156].w[7]"  1;
	setAttr ".wl[157].w[7]"  1;
	setAttr ".wl[158].w[7]"  1;
	setAttr ".wl[159].w[7]"  1;
	setAttr -s 30 ".pm";
	setAttr ".pm[0]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -8.9231745720989668 0.17376929722515433 2.0199273074892598e-15 1;
	setAttr ".pm[1]" -type "matrix" -3.4450928483976665e-16 -2.2204460492503131e-16 -1 0 -1 4.9303806576313238e-32 3.4450928483976665e-16 0
		 -7.6496428045251064e-32 1 -2.2204460492503131e-16 0 8.9231745720989668 0.17376929722515455 0.999999999999997 1;
	setAttr ".pm[2]" -type "matrix" -3.4450928483976665e-16 -2.2204460492503131e-16 -1 0 -1 4.9303806576313238e-32 3.4450928483976665e-16 0
		 -7.6496428045251064e-32 1 -2.2204460492503131e-16 0 4.6515061293712359 0.17376929722515452 0.99999999999999889 1;
	setAttr ".pm[3]" -type "matrix" 5.8331365260285766e-07 -3.4717393473770988e-07 -0.99999999999976963 0 -0.4794097213532717 0.87759120270866275 -5.8432302659159539e-07 0
		 0.87759120270866331 0.47940972135350218 3.454723706304003e-07 0 0.53189973592848949 -0.61121325699033013 1.0000005224619188 1;
	setAttr ".pm[4]" -type "matrix" -3.7839275046629232e-09 -4.9514660478913824e-07 -0.99999999999987765 0 4.5717040610908244e-16 0.99999999999987776 -4.9514660478913814e-07 0
		 1.0000000000000002 -2.2981828101998501e-15 -3.7839275046623533e-09 0 -1.0271901970466448 -0.13533431203966553 1.0000008717993354 1;
	setAttr ".pm[5]" -type "matrix" -3.7839275046629232e-09 -4.9514660478913824e-07 -0.99999999999987765 0 4.5717040610908244e-16 0.99999999999987776 -4.9514660478913814e-07 0
		 1.0000000000000002 -2.2981828101998501e-15 -3.7839275046623533e-09 0 -1.8935622781747257 -0.1353343120396657 1.0000008717993347 1;
	setAttr ".pm[6]" -type "matrix" 2.2204460492503131e-16 9.9579925010295987e-17 -1 0 1 -2.2111185107375414e-32 2.2204460492503131e-16 0
		 4.9303806576313238e-32 -1 -9.9579925010295987e-17 0 -8.9231700000000007 -0.1737689999999999 -1.000000000000002 1;
	setAttr ".pm[7]" -type "matrix" 2.2204460492503131e-16 9.9579925010295987e-17 -1 0 1 -2.2111185107375414e-32 2.2204460492503131e-16 0
		 4.9303806576313238e-32 -1 -9.9579925010295987e-17 0 -4.65151 -0.1737689999999999 -1.0000000000000011 1;
	setAttr ".pm[8]" -type "matrix" 5.8331365260285766e-07 -3.4602377056398311e-07 -0.99999999999976996 0 0.47940972135327098 -0.87759120270866364 5.8331365263106153e-07 0
		 -0.87759120270866364 -0.47940972135350091 -3.460237705164382e-07 0 -0.53189953941047974 0.61121351838277305 -1.0000005217588994 1;
	setAttr ".pm[9]" -type "matrix" -3.7839275046628231e-09 -5.0889760207317231e-07 -0.99999999999987077 0 -5.094072503275622e-16 -0.99999999999987077 5.0889760207317231e-07 0
		 -1 2.5476401720380396e-15 3.7839275046620083e-09 0 1.0271899962160689 0.13533449110186921 -1.0000010727583399 1;
	setAttr ".pm[10]" -type "matrix" -3.7839275046628231e-09 -5.0889760207317231e-07 -0.99999999999987077 0 -5.094072503275622e-16 -0.99999999999987077 5.0889760207317231e-07 0
		 -1 2.5476401720380396e-15 3.7839275046620083e-09 0 1.8935599962160683 0.13533449110186729 -1.0000010760366214 1;
	setAttr ".pm[11]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -9.5109235153967138 0.17376929722515433 2.1504337893989135e-15 1;
	setAttr ".pm[12]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -10.500223672082353 0.17376929722515433 2.3701025518424469e-15 1;
	setAttr ".pm[13]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -11.703780240227058 0.17376929722515433 2.6373457945210649e-15 1;
	setAttr ".pm[14]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -12.875926312066481 0.17376929722515433 2.8976145059570766e-15 1;
	setAttr ".pm[15]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -13.928707643645982 0.17376929722515508 3.1313789208000969e-15 1;
	setAttr ".pm[16]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -15.338164390135388 0.17376929722515508 3.444341187233257e-15 1;
	setAttr ".pm[17]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -17.042375757171094 0.17376929722515508 3.4443411872332574e-15 1;
	setAttr ".pm[18]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -0.64419300000000002 -13.5276 0.17376900000000314 1;
	setAttr ".pm[19]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -1.6150599999999999 -13.512600000000001 0.17376900000000314 1;
	setAttr ".pm[20]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -4.4291700000000001 -13.512600000000001 0.17376900000000312 1;
	setAttr ".pm[21]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -6.9456699999999998 -13.512600000000001 0.17376900000000314 1;
	setAttr ".pm[22]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -7.7752400000000002 -13.512600000000001 0.17376900000000312 1;
	setAttr ".pm[23]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -8.7057699999999993 -13.1126 0.17376900000000317 1;
	setAttr ".pm[24]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 0.64419300000000002 13.5276 -0.17376900000000289 1;
	setAttr ".pm[25]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 1.6150599999999999 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[26]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 4.4291700000000001 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[27]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 6.9456699999999998 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[28]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 7.7752400000000002 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[29]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 8.7057699999999993 13.1126 -0.17376900000000289 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 0 0 0 1;
	setAttr -s 13 ".ma";
	setAttr -s 30 ".dpf[0:29]"  4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 
		4 4 4 4 4 4 4 4 4 4;
	setAttr -s 13 ".lw";
	setAttr -s 13 ".lw";
	setAttr ".mmi" yes;
	setAttr ".mi" 5;
	setAttr ".ucm" yes;
createNode tweak -n "tweak4";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000244F";
createNode objectSet -n "skinCluster4Set";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002450";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster4GroupId";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002451";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster4GroupParts";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002452";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode objectSet -n "tweakSet4";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002453";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId8";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002454";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts8";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002455";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode skinCluster -n "skinCluster5";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002456";
	setAttr -s 26 ".wl";
	setAttr ".wl[0].w[4]"  1;
	setAttr ".wl[1].w[4]"  1;
	setAttr ".wl[2].w[4]"  1;
	setAttr ".wl[3].w[3]"  1;
	setAttr ".wl[4].w[3]"  1;
	setAttr ".wl[5].w[3]"  1;
	setAttr ".wl[6].w[3]"  1;
	setAttr ".wl[7].w[3]"  1;
	setAttr ".wl[8].w[3]"  1;
	setAttr ".wl[9].w[3]"  1;
	setAttr ".wl[10].w[3]"  1;
	setAttr ".wl[11].w[3]"  1;
	setAttr ".wl[12].w[3]"  1;
	setAttr ".wl[13].w[4]"  1;
	setAttr ".wl[14].w[4]"  1;
	setAttr ".wl[15].w[3]"  1;
	setAttr ".wl[16].w[3]"  1;
	setAttr ".wl[17].w[3]"  1;
	setAttr ".wl[18].w[3]"  1;
	setAttr ".wl[19].w[4]"  1;
	setAttr ".wl[20].w[4]"  1;
	setAttr ".wl[21].w[3]"  1;
	setAttr ".wl[22].w[3]"  1;
	setAttr ".wl[23].w[4]"  1;
	setAttr ".wl[24].w[3]"  1;
	setAttr ".wl[25].w[3]"  1;
	setAttr -s 30 ".pm";
	setAttr ".pm[0]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -8.9231745720989668 0.17376929722515433 2.0199273074892598e-15 1;
	setAttr ".pm[1]" -type "matrix" -3.4450928483976665e-16 -2.2204460492503131e-16 -1 0 -1 4.9303806576313238e-32 3.4450928483976665e-16 0
		 -7.6496428045251064e-32 1 -2.2204460492503131e-16 0 8.9231745720989668 0.17376929722515455 0.999999999999997 1;
	setAttr ".pm[2]" -type "matrix" -3.4450928483976665e-16 -2.2204460492503131e-16 -1 0 -1 4.9303806576313238e-32 3.4450928483976665e-16 0
		 -7.6496428045251064e-32 1 -2.2204460492503131e-16 0 4.6515061293712359 0.17376929722515452 0.99999999999999889 1;
	setAttr ".pm[3]" -type "matrix" 5.8331365260285766e-07 -3.4717393473770988e-07 -0.99999999999976963 0 -0.4794097213532717 0.87759120270866275 -5.8432302659159539e-07 0
		 0.87759120270866331 0.47940972135350218 3.454723706304003e-07 0 0.53189973592848949 -0.61121325699033013 1.0000005224619188 1;
	setAttr ".pm[4]" -type "matrix" -3.7839275046629232e-09 -4.9514660478913824e-07 -0.99999999999987765 0 4.5717040610908244e-16 0.99999999999987776 -4.9514660478913814e-07 0
		 1.0000000000000002 -2.2981828101998501e-15 -3.7839275046623533e-09 0 -1.0271901970466448 -0.13533431203966553 1.0000008717993354 1;
	setAttr ".pm[5]" -type "matrix" -3.7839275046629232e-09 -4.9514660478913824e-07 -0.99999999999987765 0 4.5717040610908244e-16 0.99999999999987776 -4.9514660478913814e-07 0
		 1.0000000000000002 -2.2981828101998501e-15 -3.7839275046623533e-09 0 -1.8935622781747257 -0.1353343120396657 1.0000008717993347 1;
	setAttr ".pm[6]" -type "matrix" 2.2204460492503131e-16 9.9579925010295987e-17 -1 0 1 -2.2111185107375414e-32 2.2204460492503131e-16 0
		 4.9303806576313238e-32 -1 -9.9579925010295987e-17 0 -8.9231700000000007 -0.1737689999999999 -1.000000000000002 1;
	setAttr ".pm[7]" -type "matrix" 2.2204460492503131e-16 9.9579925010295987e-17 -1 0 1 -2.2111185107375414e-32 2.2204460492503131e-16 0
		 4.9303806576313238e-32 -1 -9.9579925010295987e-17 0 -4.65151 -0.1737689999999999 -1.0000000000000011 1;
	setAttr ".pm[8]" -type "matrix" 5.8331365260285766e-07 -3.4602377056398311e-07 -0.99999999999976996 0 0.47940972135327098 -0.87759120270866364 5.8331365263106153e-07 0
		 -0.87759120270866364 -0.47940972135350091 -3.460237705164382e-07 0 -0.53189953941047974 0.61121351838277305 -1.0000005217588994 1;
	setAttr ".pm[9]" -type "matrix" -3.7839275046628231e-09 -5.0889760207317231e-07 -0.99999999999987077 0 -5.094072503275622e-16 -0.99999999999987077 5.0889760207317231e-07 0
		 -1 2.5476401720380396e-15 3.7839275046620083e-09 0 1.0271899962160689 0.13533449110186921 -1.0000010727583399 1;
	setAttr ".pm[10]" -type "matrix" -3.7839275046628231e-09 -5.0889760207317231e-07 -0.99999999999987077 0 -5.094072503275622e-16 -0.99999999999987077 5.0889760207317231e-07 0
		 -1 2.5476401720380396e-15 3.7839275046620083e-09 0 1.8935599962160683 0.13533449110186729 -1.0000010760366214 1;
	setAttr ".pm[11]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -9.5109235153967138 0.17376929722515433 2.1504337893989135e-15 1;
	setAttr ".pm[12]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -10.500223672082353 0.17376929722515433 2.3701025518424469e-15 1;
	setAttr ".pm[13]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -11.703780240227058 0.17376929722515433 2.6373457945210649e-15 1;
	setAttr ".pm[14]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -12.875926312066481 0.17376929722515433 2.8976145059570766e-15 1;
	setAttr ".pm[15]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -13.928707643645982 0.17376929722515508 3.1313789208000969e-15 1;
	setAttr ".pm[16]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -15.338164390135388 0.17376929722515508 3.444341187233257e-15 1;
	setAttr ".pm[17]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -17.042375757171094 0.17376929722515508 3.4443411872332574e-15 1;
	setAttr ".pm[18]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -0.64419300000000002 -13.5276 0.17376900000000314 1;
	setAttr ".pm[19]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -1.6150599999999999 -13.512600000000001 0.17376900000000314 1;
	setAttr ".pm[20]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -4.4291700000000001 -13.512600000000001 0.17376900000000312 1;
	setAttr ".pm[21]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -6.9456699999999998 -13.512600000000001 0.17376900000000314 1;
	setAttr ".pm[22]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -7.7752400000000002 -13.512600000000001 0.17376900000000312 1;
	setAttr ".pm[23]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -8.7057699999999993 -13.1126 0.17376900000000317 1;
	setAttr ".pm[24]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 0.64419300000000002 13.5276 -0.17376900000000289 1;
	setAttr ".pm[25]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 1.6150599999999999 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[26]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 4.4291700000000001 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[27]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 6.9456699999999998 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[28]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 7.7752400000000002 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[29]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 8.7057699999999993 13.1126 -0.17376900000000289 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 0 0 0 1;
	setAttr -s 8 ".ma";
	setAttr -s 30 ".dpf[0:29]"  4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 
		4 4 4 4 4 4 4 4 4 4;
	setAttr -s 8 ".lw";
	setAttr ".mmi" yes;
	setAttr ".mi" 5;
	setAttr ".ucm" yes;
createNode tweak -n "tweak5";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002457";
createNode objectSet -n "skinCluster5Set";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002458";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster5GroupId";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002459";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster5GroupParts";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000245A";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode objectSet -n "tweakSet5";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000245B";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId10";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000245C";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts10";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000245D";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode skinCluster -n "skinCluster6";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000245E";
	setAttr -s 26 ".wl";
	setAttr ".wl[0].w[9]"  1;
	setAttr ".wl[1].w[9]"  1;
	setAttr ".wl[2].w[9]"  1;
	setAttr ".wl[3].w[8]"  1;
	setAttr ".wl[4].w[8]"  1;
	setAttr ".wl[5].w[8]"  1;
	setAttr ".wl[6].w[8]"  1;
	setAttr ".wl[7].w[8]"  1;
	setAttr ".wl[8].w[8]"  1;
	setAttr ".wl[9].w[8]"  1;
	setAttr ".wl[10].w[8]"  1;
	setAttr ".wl[11].w[8]"  1;
	setAttr ".wl[12].w[8]"  1;
	setAttr ".wl[13].w[9]"  1;
	setAttr ".wl[14].w[9]"  1;
	setAttr ".wl[15].w[8]"  1;
	setAttr ".wl[16].w[8]"  1;
	setAttr ".wl[17].w[8]"  1;
	setAttr ".wl[18].w[8]"  1;
	setAttr ".wl[19].w[9]"  1;
	setAttr ".wl[20].w[9]"  1;
	setAttr ".wl[21].w[8]"  1;
	setAttr ".wl[22].w[8]"  1;
	setAttr ".wl[23].w[9]"  1;
	setAttr ".wl[24].w[8]"  1;
	setAttr ".wl[25].w[8]"  1;
	setAttr -s 30 ".pm";
	setAttr ".pm[0]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -8.9231745720989668 0.17376929722515433 2.0199273074892598e-15 1;
	setAttr ".pm[1]" -type "matrix" -3.4450928483976665e-16 -2.2204460492503131e-16 -1 0 -1 4.9303806576313238e-32 3.4450928483976665e-16 0
		 -7.6496428045251064e-32 1 -2.2204460492503131e-16 0 8.9231745720989668 0.17376929722515455 0.999999999999997 1;
	setAttr ".pm[2]" -type "matrix" -3.4450928483976665e-16 -2.2204460492503131e-16 -1 0 -1 4.9303806576313238e-32 3.4450928483976665e-16 0
		 -7.6496428045251064e-32 1 -2.2204460492503131e-16 0 4.6515061293712359 0.17376929722515452 0.99999999999999889 1;
	setAttr ".pm[3]" -type "matrix" 5.8331365260285766e-07 -3.4717393473770988e-07 -0.99999999999976963 0 -0.4794097213532717 0.87759120270866275 -5.8432302659159539e-07 0
		 0.87759120270866331 0.47940972135350218 3.454723706304003e-07 0 0.53189973592848949 -0.61121325699033013 1.0000005224619188 1;
	setAttr ".pm[4]" -type "matrix" -3.7839275046629232e-09 -4.9514660478913824e-07 -0.99999999999987765 0 4.5717040610908244e-16 0.99999999999987776 -4.9514660478913814e-07 0
		 1.0000000000000002 -2.2981828101998501e-15 -3.7839275046623533e-09 0 -1.0271901970466448 -0.13533431203966553 1.0000008717993354 1;
	setAttr ".pm[5]" -type "matrix" -3.7839275046629232e-09 -4.9514660478913824e-07 -0.99999999999987765 0 4.5717040610908244e-16 0.99999999999987776 -4.9514660478913814e-07 0
		 1.0000000000000002 -2.2981828101998501e-15 -3.7839275046623533e-09 0 -1.8935622781747257 -0.1353343120396657 1.0000008717993347 1;
	setAttr ".pm[6]" -type "matrix" 2.2204460492503131e-16 9.9579925010295987e-17 -1 0 1 -2.2111185107375414e-32 2.2204460492503131e-16 0
		 4.9303806576313238e-32 -1 -9.9579925010295987e-17 0 -8.9231700000000007 -0.1737689999999999 -1.000000000000002 1;
	setAttr ".pm[7]" -type "matrix" 2.2204460492503131e-16 9.9579925010295987e-17 -1 0 1 -2.2111185107375414e-32 2.2204460492503131e-16 0
		 4.9303806576313238e-32 -1 -9.9579925010295987e-17 0 -4.65151 -0.1737689999999999 -1.0000000000000011 1;
	setAttr ".pm[8]" -type "matrix" 5.8331365260285766e-07 -3.4602377056398311e-07 -0.99999999999976996 0 0.47940972135327098 -0.87759120270866364 5.8331365263106153e-07 0
		 -0.87759120270866364 -0.47940972135350091 -3.460237705164382e-07 0 -0.53189953941047974 0.61121351838277305 -1.0000005217588994 1;
	setAttr ".pm[9]" -type "matrix" -3.7839275046628231e-09 -5.0889760207317231e-07 -0.99999999999987077 0 -5.094072503275622e-16 -0.99999999999987077 5.0889760207317231e-07 0
		 -1 2.5476401720380396e-15 3.7839275046620083e-09 0 1.0271899962160689 0.13533449110186921 -1.0000010727583399 1;
	setAttr ".pm[10]" -type "matrix" -3.7839275046628231e-09 -5.0889760207317231e-07 -0.99999999999987077 0 -5.094072503275622e-16 -0.99999999999987077 5.0889760207317231e-07 0
		 -1 2.5476401720380396e-15 3.7839275046620083e-09 0 1.8935599962160683 0.13533449110186729 -1.0000010760366214 1;
	setAttr ".pm[11]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -9.5109235153967138 0.17376929722515433 2.1504337893989135e-15 1;
	setAttr ".pm[12]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -10.500223672082353 0.17376929722515433 2.3701025518424469e-15 1;
	setAttr ".pm[13]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -11.703780240227058 0.17376929722515433 2.6373457945210649e-15 1;
	setAttr ".pm[14]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -12.875926312066481 0.17376929722515433 2.8976145059570766e-15 1;
	setAttr ".pm[15]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -13.928707643645982 0.17376929722515508 3.1313789208000969e-15 1;
	setAttr ".pm[16]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -15.338164390135388 0.17376929722515508 3.444341187233257e-15 1;
	setAttr ".pm[17]" -type "matrix" 2.2204460492503131e-16 -2.2204460492503131e-16 1 0 1 4.9303806576313238e-32 -2.2204460492503131e-16 0
		 4.9303806576313238e-32 1 2.2204460492503131e-16 0 -17.042375757171094 0.17376929722515508 3.4443411872332574e-15 1;
	setAttr ".pm[18]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -0.64419300000000002 -13.5276 0.17376900000000314 1;
	setAttr ".pm[19]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -1.6150599999999999 -13.512600000000001 0.17376900000000314 1;
	setAttr ".pm[20]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -4.4291700000000001 -13.512600000000001 0.17376900000000312 1;
	setAttr ".pm[21]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -6.9456699999999998 -13.512600000000001 0.17376900000000314 1;
	setAttr ".pm[22]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -7.7752400000000002 -13.512600000000001 0.17376900000000312 1;
	setAttr ".pm[23]" -type "matrix" 1 -4.9303806576313238e-32 -2.2204460492503131e-16 0 0 1 -2.2204460492503126e-16 0
		 2.2204460492503136e-16 2.2204460492503131e-16 1 0 -8.7057699999999993 -13.1126 0.17376900000000317 1;
	setAttr ".pm[24]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 0.64419300000000002 13.5276 -0.17376900000000289 1;
	setAttr ".pm[25]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 1.6150599999999999 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[26]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 4.4291700000000001 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[27]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 6.9456699999999998 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[28]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 7.7752400000000002 13.512600000000001 -0.17376900000000289 1;
	setAttr ".pm[29]" -type "matrix" 1 4.9303806576313238e-32 2.2204460492503131e-16 0 0 -1 2.2204460492503126e-16 0
		 2.2204460492503136e-16 -2.2204460492503131e-16 -1 0 8.7057699999999993 13.1126 -0.17376900000000289 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 0 0 0 1;
	setAttr -s 8 ".ma";
	setAttr -s 30 ".dpf[0:29]"  4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 
		4 4 4 4 4 4 4 4 4 4;
	setAttr -s 8 ".lw";
	setAttr ".mmi" yes;
	setAttr ".mi" 5;
	setAttr ".ucm" yes;
createNode tweak -n "tweak6";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000245F";
createNode objectSet -n "skinCluster6Set";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002460";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster6GroupId";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002461";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster6GroupParts";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002462";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode objectSet -n "tweakSet6";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002463";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId12";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002464";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts12";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002465";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode partition -n "mtorPartition";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002466";
	addAttr -s false -ci true -sn "rgcnx" -ln "rgcnx" -at "message";
	addAttr -ci true -sn "sd" -ln "slimData" -dt "string";
	addAttr -ci true -sn "sr" -ln "slimRIB" -dt "string";
	addAttr -ci true -sn "rd" -ln "rlfData" -dt "string";
	setAttr ".sr" -type "string" "";
createNode script -n "xgenGlobals";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002467";
	setAttr ".a" -type "string" "import maya.cmds as cmds\nif cmds.about(batch=True):\n\txgg.Playblast=False\nelse:\n\txgui.createDescriptionEditor(False).setGlobals( previewSel=0, previewMode=0, clearSel=0, clearMode=0, playblast=1, clearCache=0, autoCreateMR=1 )";
	setAttr ".stp" 1;
createNode lambert -n "lambert3";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002468";
	setAttr ".c" -type "float3" 0.88235295 0.87271333 0.55363321 ;
createNode shadingEngine -n "lambert3SG";
	rename -uid "D3D318C0-0000-1586-5B67-E79100002469";
	setAttr ".ihi" 0;
	setAttr -s 6 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo2";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000246A";
createNode HIKCharacterNode -n "Character1";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000246B";
	setAttr ".HipsTx" 0.039231777000000002;
	setAttr ".HipsTy" 8.918911;
	setAttr ".HipsTz" -0.16478749000000001;
	setAttr ".HipsRx" 90;
	setAttr ".HipsRz" 90;
	setAttr ".HipsJointOrientx" 89.999999999999986;
	setAttr ".HipsJointOrientz" 89.999999999999986;
	setAttr ".HipsMinRLimitx" -45;
	setAttr ".HipsMinRLimity" -45;
	setAttr ".HipsMinRLimitz" -45;
	setAttr ".HipsMaxRLimitx" 45;
	setAttr ".HipsMaxRLimity" 45;
	setAttr ".HipsMaxRLimitz" 45;
	setAttr ".LeftUpLegTx" 1.0392317769999999;
	setAttr ".LeftUpLegTy" 8.918911;
	setAttr ".LeftUpLegTz" -0.16478749000000001;
	setAttr ".LeftUpLegRx" 90.000143472185755;
	setAttr ".LeftUpLegRy" 1.8240684774494309;
	setAttr ".LeftUpLegRz" -89.990987556490538;
	setAttr ".LeftUpLegSx" 1.0000000000000002;
	setAttr ".LeftUpLegSy" 0.99999999999999989;
	setAttr ".LeftUpLegJointOrienty" 180;
	setAttr ".LeftUpLegMinRLimitx" -45;
	setAttr ".LeftUpLegMinRLimity" -45;
	setAttr ".LeftUpLegMinRLimitz" -45;
	setAttr ".LeftUpLegMaxRLimitx" 45;
	setAttr ".LeftUpLegMaxRLimity" 45;
	setAttr ".LeftUpLegMaxRLimitz" 45;
	setAttr ".LeftLegTx" 1.0399033563519851;
	setAttr ".LeftLegTy" 4.6494071613307719;
	setAttr ".LeftLegTz" -0.3007573585954656;
	setAttr ".LeftLegRx" 90.000143364148713;
	setAttr ".LeftLegRy" 1.8636444374578627;
	setAttr ".LeftLegRz" -89.990990877508736;
	setAttr ".LeftLegSx" 1.0000000000000002;
	setAttr ".LeftLegSy" 0.99999999999999989;
	setAttr ".LeftLegMinRLimitx" -45;
	setAttr ".LeftLegMinRLimity" -45;
	setAttr ".LeftLegMinRLimitz" -45;
	setAttr ".LeftLegMaxRLimitx" 45;
	setAttr ".LeftLegMaxRLimity" 45;
	setAttr ".LeftLegMaxRLimitz" 45;
	setAttr ".LeftFootTx" 1.0405099949136352;
	setAttr ".LeftFootTy" 0.79133674218856775;
	setAttr ".LeftFootTz" -0.42629205539076853;
	setAttr ".LeftFootRx" 90;
	setAttr ".LeftFootRy" -61.353143481144123;
	setAttr ".LeftFootRz" -90;
	setAttr ".LeftFootSx" 0.99999999999981648;
	setAttr ".LeftFootSy" 0.99999999999994038;
	setAttr ".LeftFootSz" 0.99999999999975642;
	setAttr ".LeftFootJointOrientx" 1.9891601228648406e-05;
	setAttr ".LeftFootJointOrienty" 3.3421410447133865e-05;
	setAttr ".LeftFootJointOrientz" 61.353142918098186;
	setAttr ".LeftFootMinRLimitx" -45;
	setAttr ".LeftFootMinRLimity" -45;
	setAttr ".LeftFootMinRLimitz" -45;
	setAttr ".LeftFootMaxRLimitx" 45;
	setAttr ".LeftFootMaxRLimity" 45;
	setAttr ".LeftFootMaxRLimitz" 45;
	setAttr ".RightUpLegTx" -0.96076822299999998;
	setAttr ".RightUpLegTy" 8.9189064279010335;
	setAttr ".RightUpLegTz" -0.16478719277484569;
	setAttr ".RightUpLegRx" -90.00013997856675;
	setAttr ".RightUpLegRy" -1.7810400780148388;
	setAttr ".RightUpLegRz" 90.00900545193501;
	setAttr ".RightUpLegSy" 1.0000000000000002;
	setAttr ".RightUpLegSz" 1.0000000000000002;
	setAttr ".RightUpLegJointOrientx" -180;
	setAttr ".RightUpLegMinRLimitx" -45;
	setAttr ".RightUpLegMinRLimity" -45;
	setAttr ".RightUpLegMinRLimitz" -45;
	setAttr ".RightUpLegMaxRLimitx" 45;
	setAttr ".RightUpLegMaxRLimity" 45;
	setAttr ".RightUpLegMaxRLimitz" 45;
	setAttr ".RightLegTx" -0.96009715010466756;
	setAttr ".RightLegTy" 4.6493101201343334;
	setAttr ".RightLegTz" -0.29755041797722603;
	setAttr ".RightLegRx" -90.000148543839629;
	setAttr ".RightLegRy" -1.9112660680099156;
	setAttr ".RightLegRz" 90.009007626883815;
	setAttr ".RightLegSz" 1.0000000000000002;
	setAttr ".RightLegMinRLimitx" -45;
	setAttr ".RightLegMinRLimity" -45;
	setAttr ".RightLegMinRLimitz" -45;
	setAttr ".RightLegMaxRLimitx" 45;
	setAttr ".RightLegMaxRLimity" 45;
	setAttr ".RightLegMaxRLimitz" 45;
	setAttr ".RightFootTx" -0.95949062827707021;
	setAttr ".RightFootTy" 0.79134163789417178;
	setAttr ".RightFootTz" -0.42629184731843955;
	setAttr ".RightFootRx" -90;
	setAttr ".RightFootRy" 61.353143243898813;
	setAttr ".RightFootRz" 90;
	setAttr ".RightFootSx" 0.99999999999981415;
	setAttr ".RightFootSy" 0.99999999999994071;
	setAttr ".RightFootSz" 0.99999999999975475;
	setAttr ".RightFootJointOrientx" 1.9825701656093505e-05;
	setAttr ".RightFootJointOrienty" 3.3421410415399674e-05;
	setAttr ".RightFootJointOrientz" 61.353142918098222;
	setAttr ".RightFootMinRLimitx" -45;
	setAttr ".RightFootMinRLimity" -45;
	setAttr ".RightFootMinRLimitz" -45;
	setAttr ".RightFootMaxRLimitx" 45;
	setAttr ".RightFootMaxRLimity" 45;
	setAttr ".RightFootMaxRLimitz" 45;
	setAttr ".SpineTx" 0.039231777000000002;
	setAttr ".SpineTy" 9.5066599432977466;
	setAttr ".SpineTz" -0.16478749000000001;
	setAttr ".SpineRx" 90;
	setAttr ".SpineRz" 90;
	setAttr ".SpineMinRLimitx" -45;
	setAttr ".SpineMinRLimity" -45;
	setAttr ".SpineMinRLimitz" -45;
	setAttr ".SpineMaxRLimitx" 45;
	setAttr ".SpineMaxRLimity" 45;
	setAttr ".SpineMaxRLimitz" 45;
	setAttr ".LeftArmTx" 1.6542917770000001;
	setAttr ".LeftArmTy" 13.508336427901034;
	setAttr ".LeftArmTz" -0.16478719277484546;
	setAttr ".LeftArmMinRLimitx" -45;
	setAttr ".LeftArmMinRLimity" -45;
	setAttr ".LeftArmMinRLimitz" -45;
	setAttr ".LeftArmMaxRLimitx" 45;
	setAttr ".LeftArmMaxRLimity" 45;
	setAttr ".LeftArmMaxRLimitz" 45;
	setAttr ".LeftForeArmTx" 4.4684017770000004;
	setAttr ".LeftForeArmTy" 13.508336427901034;
	setAttr ".LeftForeArmTz" -0.16478719277484483;
	setAttr ".LeftForeArmMinRLimitx" -45;
	setAttr ".LeftForeArmMinRLimity" -45;
	setAttr ".LeftForeArmMinRLimitz" -45;
	setAttr ".LeftForeArmMaxRLimitx" 45;
	setAttr ".LeftForeArmMaxRLimity" 45;
	setAttr ".LeftForeArmMaxRLimitz" 45;
	setAttr ".LeftHandTx" 6.9849017770000001;
	setAttr ".LeftHandTy" 13.508336427901034;
	setAttr ".LeftHandTz" -0.16478719277484427;
	setAttr ".LeftHandMinRLimitx" -45;
	setAttr ".LeftHandMinRLimity" -45;
	setAttr ".LeftHandMinRLimitz" -45;
	setAttr ".LeftHandMaxRLimitx" 45;
	setAttr ".LeftHandMaxRLimity" 45;
	setAttr ".LeftHandMaxRLimitz" 45;
	setAttr ".RightArmTx" -1.575828223;
	setAttr ".RightArmTy" 13.508336427901034;
	setAttr ".RightArmTz" -0.16478719277484591;
	setAttr ".RightArmRx" 180;
	setAttr ".RightArmMinRLimitx" -45;
	setAttr ".RightArmMinRLimity" -45;
	setAttr ".RightArmMinRLimitz" -45;
	setAttr ".RightArmMaxRLimitx" 45;
	setAttr ".RightArmMaxRLimity" 45;
	setAttr ".RightArmMaxRLimitz" 45;
	setAttr ".RightForeArmTx" -4.3899382230000006;
	setAttr ".RightForeArmTy" 13.508336427901034;
	setAttr ".RightForeArmTz" -0.16478719277484655;
	setAttr ".RightForeArmRx" 180;
	setAttr ".RightForeArmMinRLimitx" -45;
	setAttr ".RightForeArmMinRLimity" -45;
	setAttr ".RightForeArmMinRLimitz" -45;
	setAttr ".RightForeArmMaxRLimitx" 45;
	setAttr ".RightForeArmMaxRLimity" 45;
	setAttr ".RightForeArmMaxRLimitz" 45;
	setAttr ".RightHandTx" -6.9064382230000003;
	setAttr ".RightHandTy" 13.508336427901034;
	setAttr ".RightHandTz" -0.1647871927748471;
	setAttr ".RightHandRx" 180;
	setAttr ".RightHandMinRLimitx" -45;
	setAttr ".RightHandMinRLimity" -45;
	setAttr ".RightHandMinRLimitz" -45;
	setAttr ".RightHandMaxRLimitx" 45;
	setAttr ".RightHandMaxRLimity" 45;
	setAttr ".RightHandMaxRLimitz" 45;
	setAttr ".HeadTx" 0.039231777000000002;
	setAttr ".HeadTy" 15.333900818036421;
	setAttr ".HeadTz" -0.16478749000000076;
	setAttr ".HeadRx" 90;
	setAttr ".HeadRz" 90;
	setAttr ".HeadMinRLimitx" -45;
	setAttr ".HeadMinRLimity" -45;
	setAttr ".HeadMinRLimitz" -45;
	setAttr ".HeadMaxRLimitx" 45;
	setAttr ".HeadMaxRLimity" 45;
	setAttr ".HeadMaxRLimitz" 45;
	setAttr ".LeftToeBaseTx" 1.0405108269728094;
	setAttr ".LeftToeBaseTy" 0.1352776953507876;
	setAttr ".LeftToeBaseTz" 0.77466744911204066;
	setAttr ".LeftToeBaseRy" -90;
	setAttr ".LeftToeBaseSx" 0.99999999999999989;
	setAttr ".LeftToeBaseSy" 0.99999999999987266;
	setAttr ".LeftToeBaseSz" 0.99999999999987221;
	setAttr ".LeftToeBaseJointOrientx" -5.109432601362014e-06;
	setAttr ".LeftToeBaseJointOrienty" -2.0010911851502281e-05;
	setAttr ".LeftToeBaseJointOrientz" 28.646857081913563;
	setAttr ".LeftToeBaseMinRLimitx" -45;
	setAttr ".LeftToeBaseMinRLimity" -45;
	setAttr ".LeftToeBaseMinRLimitz" -45;
	setAttr ".LeftToeBaseMaxRLimitx" 45;
	setAttr ".LeftToeBaseMaxRLimity" 45;
	setAttr ".LeftToeBaseMaxRLimitz" 45;
	setAttr ".RightToeBaseTx" -0.95949166473131353;
	setAttr ".RightToeBaseTy" 0.13528264472318974;
	setAttr ".RightToeBaseTz" 0.77466715641208039;
	setAttr ".RightToeBaseRx" -180;
	setAttr ".RightToeBaseRy" 90;
	setAttr ".RightToeBaseSy" 0.99999999999986477;
	setAttr ".RightToeBaseSz" 0.99999999999986455;
	setAttr ".RightToeBaseJointOrientx" -4.2637256250019046e-06;
	setAttr ".RightToeBaseJointOrienty" -2.0042504737796228e-05;
	setAttr ".RightToeBaseJointOrientz" 28.646857081913506;
	setAttr ".RightToeBaseMinRLimitx" -45;
	setAttr ".RightToeBaseMinRLimity" -45;
	setAttr ".RightToeBaseMinRLimitz" -45;
	setAttr ".RightToeBaseMaxRLimitx" 45;
	setAttr ".RightToeBaseMaxRLimity" 45;
	setAttr ".RightToeBaseMaxRLimitz" 45;
	setAttr ".LeftShoulderTx" 0.68342477700000004;
	setAttr ".LeftShoulderTy" 13.523336427901032;
	setAttr ".LeftShoulderTz" -0.16478719277484569;
	setAttr ".LeftShoulderJointOrientx" -89.999999999999986;
	setAttr ".LeftShoulderJointOrienty" -89.999999999999986;
	setAttr ".LeftShoulderMinRLimitx" -45;
	setAttr ".LeftShoulderMinRLimity" -45;
	setAttr ".LeftShoulderMinRLimitz" -45;
	setAttr ".LeftShoulderMaxRLimitx" 45;
	setAttr ".LeftShoulderMaxRLimity" 45;
	setAttr ".LeftShoulderMaxRLimitz" 45;
	setAttr ".RightShoulderTx" -0.60496122299999999;
	setAttr ".RightShoulderTy" 13.523336427901032;
	setAttr ".RightShoulderTz" -0.16478719277484569;
	setAttr ".RightShoulderRx" 180;
	setAttr ".RightShoulderJointOrientx" 90.000000000000014;
	setAttr ".RightShoulderJointOrienty" -89.999999999999986;
	setAttr ".RightShoulderMinRLimitx" -45;
	setAttr ".RightShoulderMinRLimity" -45;
	setAttr ".RightShoulderMinRLimitz" -45;
	setAttr ".RightShoulderMaxRLimitx" 45;
	setAttr ".RightShoulderMaxRLimity" 45;
	setAttr ".RightShoulderMaxRLimitz" 45;
	setAttr ".NeckTx" 0.039231777000000002;
	setAttr ".NeckTy" 13.924444071547015;
	setAttr ".NeckTz" -0.16478749000000076;
	setAttr ".NeckRx" 90;
	setAttr ".NeckRz" 90;
	setAttr ".NeckMinRLimitx" -45;
	setAttr ".NeckMinRLimity" -45;
	setAttr ".NeckMinRLimitz" -45;
	setAttr ".NeckMaxRLimitx" 45;
	setAttr ".NeckMaxRLimity" 45;
	setAttr ".NeckMaxRLimitz" 45;
	setAttr ".Spine1Tx" 0.039231777000000002;
	setAttr ".Spine1Ty" 10.495960099983384;
	setAttr ".Spine1Tz" -0.16478749000000001;
	setAttr ".Spine1Rx" 90;
	setAttr ".Spine1Rz" 90;
	setAttr ".Spine1MinRLimitx" -45;
	setAttr ".Spine1MinRLimity" -45;
	setAttr ".Spine1MinRLimitz" -45;
	setAttr ".Spine1MaxRLimitx" 45;
	setAttr ".Spine1MaxRLimity" 45;
	setAttr ".Spine1MaxRLimitz" 45;
	setAttr ".Spine2Tx" 0.039231777000000002;
	setAttr ".Spine2Ty" 11.699516668128091;
	setAttr ".Spine2Tz" -0.16478749000000001;
	setAttr ".Spine2Rx" 90;
	setAttr ".Spine2Rz" 90;
	setAttr ".Spine2MinRLimitx" -45;
	setAttr ".Spine2MinRLimity" -45;
	setAttr ".Spine2MinRLimitz" -45;
	setAttr ".Spine2MaxRLimitx" 45;
	setAttr ".Spine2MaxRLimity" 45;
	setAttr ".Spine2MaxRLimitz" 45;
createNode HIKProperty2State -n "HIKproperties1";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000246C";
createNode nodeGraphEditorBookmarkInfo -n "nodeGraphEditorBookmarkInfo1";
	rename -uid "D3D318C0-0000-1586-5B67-E7910000246D";
	setAttr ".vl" -type "double2" -235.08874510661417 -16.291625546268918 ;
	setAttr ".vh" -type "double2" 235.26839775052875 15.851231596588228 ;
	setAttr ".ni[0].nvs" 1920;
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "D3D318C0-0000-1586-5B67-E7920000246E";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "D3D318C0-0000-1586-5B67-E7920000246F";
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 18 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surfaces" "Particles" "Fluids" "Image Planes" "UI:" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 18 0 1 1 1 1 1
		 1 0 0 0 0 0 0 0 0 0 0 0 ;
select -ne :renderPartition;
	setAttr -s 9 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 5 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :defaultColorMgtGlobals;
	setAttr ".cme" no;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
connectAttr "Crw_Hips.s" "Crw_LeftUpLeg.is";
connectAttr "Crw_LeftUpLeg.s" "Crw_LeftLeg.is";
connectAttr "Crw_LeftLeg.s" "Crw_LeftFoot.is";
connectAttr "Crw_LeftFoot.s" "Crw_LeftToeBase.is";
connectAttr "Crw_LeftToeBase.s" "Crw_LeftToe.is";
connectAttr "Crw_Hips.s" "Crw_RightUpLeg.is";
connectAttr "Crw_RightUpLeg.s" "Crw_RightLeg.is";
connectAttr "Crw_RightLeg.s" "Crw_RightFoot.is";
connectAttr "Crw_RightFoot.s" "Crw_RightToeBase.is";
connectAttr "Crw_RightToeBase.s" "Crw_RightToe.is";
connectAttr "Crw_Hips.s" "Crw_Spine.is";
connectAttr "Crw_Spine.s" "Crw_Spine1.is";
connectAttr "Crw_Spine1.s" "Crw_Spine2.is";
connectAttr "Crw_Spine2.s" "Crw_Spine3.is";
connectAttr "Crw_Spine3.s" "Crw_Neck.is";
connectAttr "Crw_Neck.s" "Crw_Head.is";
connectAttr "Crw_Head.s" "Crw_Hair.is";
connectAttr "Crw_Hair.s" "Crw_hairTip.is";
connectAttr "Crw_Spine3.s" "Crw_LeftShoulder.is";
connectAttr "Crw_LeftShoulder.s" "Crw_LeftArm.is";
connectAttr "Crw_LeftArm.s" "Crw_LeftForeArm.is";
connectAttr "Crw_LeftForeArm.s" "Crw_LeftHand.is";
connectAttr "Crw_LeftHand.s" "Crw_LefthandSub1.is";
connectAttr "Crw_LefthandSub1.s" "Crw_LefthandSub2.is";
connectAttr "Crw_Spine3.s" "Crw_RightShoulder.is";
connectAttr "Crw_RightShoulder.s" "Crw_RightArm.is";
connectAttr "Crw_RightArm.s" "Crw_RightForeArm.is";
connectAttr "Crw_RightForeArm.s" "Crw_RightHand.is";
connectAttr "Crw_RightHand.s" "Crw_RightHandSub1.is";
connectAttr "Crw_RightHandSub1.s" "Crw_RightHandSub2.is";
connectAttr "skinCluster1GroupId.id" "mocap_shirt_PLYShape.iog.og[0].gid";
connectAttr "skinCluster1Set.mwc" "mocap_shirt_PLYShape.iog.og[0].gco";
connectAttr "groupId2.id" "mocap_shirt_PLYShape.iog.og[1].gid";
connectAttr "tweakSet1.mwc" "mocap_shirt_PLYShape.iog.og[1].gco";
connectAttr "skinCluster1.og[0]" "mocap_shirt_PLYShape.i";
connectAttr "tweak1.vl[0].vt[0]" "mocap_shirt_PLYShape.twl";
connectAttr "skinCluster2GroupId.id" "mocap_head_PLYShape.iog.og[0].gid";
connectAttr "skinCluster2Set.mwc" "mocap_head_PLYShape.iog.og[0].gco";
connectAttr "groupId4.id" "mocap_head_PLYShape.iog.og[1].gid";
connectAttr "tweakSet2.mwc" "mocap_head_PLYShape.iog.og[1].gco";
connectAttr "skinCluster2.og[0]" "mocap_head_PLYShape.i";
connectAttr "tweak2.vl[0].vt[0]" "mocap_head_PLYShape.twl";
connectAttr "skinCluster3GroupId.id" "mocap_arm_PLYShape.iog.og[0].gid";
connectAttr "skinCluster3Set.mwc" "mocap_arm_PLYShape.iog.og[0].gco";
connectAttr "groupId6.id" "mocap_arm_PLYShape.iog.og[1].gid";
connectAttr "tweakSet3.mwc" "mocap_arm_PLYShape.iog.og[1].gco";
connectAttr "skinCluster3.og[0]" "mocap_arm_PLYShape.i";
connectAttr "tweak3.vl[0].vt[0]" "mocap_arm_PLYShape.twl";
connectAttr "skinCluster4GroupId.id" "mocap_pant_PLYShape.iog.og[0].gid";
connectAttr "skinCluster4Set.mwc" "mocap_pant_PLYShape.iog.og[0].gco";
connectAttr "groupId8.id" "mocap_pant_PLYShape.iog.og[1].gid";
connectAttr "tweakSet4.mwc" "mocap_pant_PLYShape.iog.og[1].gco";
connectAttr "skinCluster4.og[0]" "mocap_pant_PLYShape.i";
connectAttr "tweak4.vl[0].vt[0]" "mocap_pant_PLYShape.twl";
connectAttr "skinCluster5GroupId.id" "mocap_shoe_L_PLYShape.iog.og[0].gid";
connectAttr "skinCluster5Set.mwc" "mocap_shoe_L_PLYShape.iog.og[0].gco";
connectAttr "groupId10.id" "mocap_shoe_L_PLYShape.iog.og[1].gid";
connectAttr "tweakSet5.mwc" "mocap_shoe_L_PLYShape.iog.og[1].gco";
connectAttr "skinCluster5.og[0]" "mocap_shoe_L_PLYShape.i";
connectAttr "tweak5.vl[0].vt[0]" "mocap_shoe_L_PLYShape.twl";
connectAttr "skinCluster6GroupId.id" "mocap_shoe_R_PLYShape.iog.og[0].gid";
connectAttr "skinCluster6Set.mwc" "mocap_shoe_R_PLYShape.iog.og[0].gco";
connectAttr "groupId12.id" "mocap_shoe_R_PLYShape.iog.og[1].gid";
connectAttr "tweakSet6.mwc" "mocap_shoe_R_PLYShape.iog.og[1].gco";
connectAttr "skinCluster6.og[0]" "mocap_shoe_R_PLYShape.i";
connectAttr "tweak6.vl[0].vt[0]" "mocap_shoe_R_PLYShape.twl";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "initialShadingGroup1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert2SG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "initialShadingGroup2.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert2SG2.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "initialShadingGroup3.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":ikSystem.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert3SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "initialShadingGroup1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert2SG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "initialShadingGroup2.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert2SG2.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "initialShadingGroup3.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert3SG.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr ":mentalrayGlobals.msg" ":mentalrayItemsList.glb";
connectAttr ":miDefaultOptions.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":miDefaultFramebuffer.msg" ":mentalrayItemsList.fb" -na;
connectAttr ":miDefaultOptions.msg" ":mentalrayGlobals.opt";
connectAttr ":miDefaultFramebuffer.msg" ":mentalrayGlobals.fb";
connectAttr "lambert2SG.msg" "materialInfo1.sg";
connectAttr "initialShadingGroup1.msg" "materialInfo3.sg";
connectAttr "lambert2SG1.msg" "materialInfo4.sg";
connectAttr "initialShadingGroup2.msg" "materialInfo5.sg";
connectAttr "lambert2SG2.msg" "materialInfo6.sg";
connectAttr "initialShadingGroup3.msg" "materialInfo7.sg";
connectAttr "Crw_Hips.msg" "bindPose1.m[0]";
connectAttr "Crw_LeftUpLeg.msg" "bindPose1.m[1]";
connectAttr "Crw_LeftLeg.msg" "bindPose1.m[2]";
connectAttr "Crw_LeftFoot.msg" "bindPose1.m[3]";
connectAttr "Crw_LeftToeBase.msg" "bindPose1.m[4]";
connectAttr "Crw_RightUpLeg.msg" "bindPose1.m[6]";
connectAttr "Crw_RightLeg.msg" "bindPose1.m[7]";
connectAttr "Crw_RightFoot.msg" "bindPose1.m[8]";
connectAttr "Crw_RightToeBase.msg" "bindPose1.m[9]";
connectAttr "Crw_Spine.msg" "bindPose1.m[11]";
connectAttr "Crw_Spine1.msg" "bindPose1.m[12]";
connectAttr "Crw_Spine2.msg" "bindPose1.m[13]";
connectAttr "Crw_Spine3.msg" "bindPose1.m[14]";
connectAttr "Crw_Neck.msg" "bindPose1.m[15]";
connectAttr "Crw_Head.msg" "bindPose1.m[16]";
connectAttr "Crw_LeftShoulder.msg" "bindPose1.m[18]";
connectAttr "Crw_LeftArm.msg" "bindPose1.m[19]";
connectAttr "Crw_LeftForeArm.msg" "bindPose1.m[20]";
connectAttr "Crw_LeftHand.msg" "bindPose1.m[21]";
connectAttr "Crw_LefthandSub1.msg" "bindPose1.m[22]";
connectAttr "Crw_RightShoulder.msg" "bindPose1.m[24]";
connectAttr "Crw_RightArm.msg" "bindPose1.m[25]";
connectAttr "Crw_RightForeArm.msg" "bindPose1.m[26]";
connectAttr "Crw_RightHand.msg" "bindPose1.m[27]";
connectAttr "Crw_RightHandSub1.msg" "bindPose1.m[28]";
connectAttr "Crw_Hair.msg" "bindPose1.m[36]";
connectAttr "Crw_LefthandSub2.msg" "bindPose1.m[41]";
connectAttr "Crw_RightHandSub2.msg" "bindPose1.m[42]";
connectAttr "Crw_LeftToe.msg" "bindPose1.m[43]";
connectAttr "Crw_RightToe.msg" "bindPose1.m[44]";
connectAttr "Crw_hairTip.msg" "bindPose1.m[46]";
connectAttr "bindPose1.w" "bindPose1.p[0]";
connectAttr "bindPose1.m[0]" "bindPose1.p[1]";
connectAttr "bindPose1.m[1]" "bindPose1.p[2]";
connectAttr "bindPose1.m[2]" "bindPose1.p[3]";
connectAttr "bindPose1.m[3]" "bindPose1.p[4]";
connectAttr "bindPose1.m[0]" "bindPose1.p[6]";
connectAttr "bindPose1.m[6]" "bindPose1.p[7]";
connectAttr "bindPose1.m[7]" "bindPose1.p[8]";
connectAttr "bindPose1.m[8]" "bindPose1.p[9]";
connectAttr "bindPose1.m[0]" "bindPose1.p[11]";
connectAttr "bindPose1.m[11]" "bindPose1.p[12]";
connectAttr "bindPose1.m[12]" "bindPose1.p[13]";
connectAttr "bindPose1.m[13]" "bindPose1.p[14]";
connectAttr "bindPose1.m[14]" "bindPose1.p[15]";
connectAttr "bindPose1.m[15]" "bindPose1.p[16]";
connectAttr "bindPose1.m[14]" "bindPose1.p[18]";
connectAttr "bindPose1.m[18]" "bindPose1.p[19]";
connectAttr "bindPose1.m[19]" "bindPose1.p[20]";
connectAttr "bindPose1.m[20]" "bindPose1.p[21]";
connectAttr "bindPose1.m[21]" "bindPose1.p[22]";
connectAttr "bindPose1.m[14]" "bindPose1.p[24]";
connectAttr "bindPose1.m[24]" "bindPose1.p[25]";
connectAttr "bindPose1.m[25]" "bindPose1.p[26]";
connectAttr "bindPose1.m[26]" "bindPose1.p[27]";
connectAttr "bindPose1.m[27]" "bindPose1.p[28]";
connectAttr "bindPose1.m[16]" "bindPose1.p[36]";
connectAttr "bindPose1.m[22]" "bindPose1.p[41]";
connectAttr "bindPose1.m[28]" "bindPose1.p[42]";
connectAttr "bindPose1.m[4]" "bindPose1.p[43]";
connectAttr "bindPose1.m[9]" "bindPose1.p[44]";
connectAttr "bindPose1.m[36]" "bindPose1.p[46]";
connectAttr "Crw_Hips.bps" "bindPose1.wm[0]";
connectAttr "Crw_LeftUpLeg.bps" "bindPose1.wm[1]";
connectAttr "Crw_LeftLeg.bps" "bindPose1.wm[2]";
connectAttr "Crw_LeftFoot.bps" "bindPose1.wm[3]";
connectAttr "Crw_LeftToeBase.bps" "bindPose1.wm[4]";
connectAttr "Crw_RightUpLeg.bps" "bindPose1.wm[6]";
connectAttr "Crw_RightLeg.bps" "bindPose1.wm[7]";
connectAttr "Crw_RightFoot.bps" "bindPose1.wm[8]";
connectAttr "Crw_RightToeBase.bps" "bindPose1.wm[9]";
connectAttr "Crw_Spine.bps" "bindPose1.wm[11]";
connectAttr "Crw_Spine1.bps" "bindPose1.wm[12]";
connectAttr "Crw_Spine2.bps" "bindPose1.wm[13]";
connectAttr "Crw_Spine3.bps" "bindPose1.wm[14]";
connectAttr "Crw_Neck.bps" "bindPose1.wm[15]";
connectAttr "Crw_Head.bps" "bindPose1.wm[16]";
connectAttr "Crw_LeftShoulder.bps" "bindPose1.wm[18]";
connectAttr "Crw_LeftArm.bps" "bindPose1.wm[19]";
connectAttr "Crw_LeftForeArm.bps" "bindPose1.wm[20]";
connectAttr "Crw_LeftHand.bps" "bindPose1.wm[21]";
connectAttr "Crw_LefthandSub1.bps" "bindPose1.wm[22]";
connectAttr "Crw_RightShoulder.bps" "bindPose1.wm[24]";
connectAttr "Crw_RightArm.bps" "bindPose1.wm[25]";
connectAttr "Crw_RightForeArm.bps" "bindPose1.wm[26]";
connectAttr "Crw_RightHand.bps" "bindPose1.wm[27]";
connectAttr "Crw_RightHandSub1.bps" "bindPose1.wm[28]";
connectAttr "Crw_Hair.bps" "bindPose1.wm[36]";
connectAttr "Crw_LefthandSub2.bps" "bindPose1.wm[41]";
connectAttr "Crw_RightHandSub2.bps" "bindPose1.wm[42]";
connectAttr "Crw_LeftToe.bps" "bindPose1.wm[43]";
connectAttr "Crw_RightToe.bps" "bindPose1.wm[44]";
connectAttr "Crw_hairTip.bps" "bindPose1.wm[46]";
connectAttr "skinCluster1GroupParts.og" "skinCluster1.ip[0].ig";
connectAttr "skinCluster1GroupId.id" "skinCluster1.ip[0].gi";
connectAttr "Crw_Hips.wm" "skinCluster1.ma[0]";
connectAttr "Crw_LeftUpLeg.wm" "skinCluster1.ma[1]";
connectAttr "Crw_RightUpLeg.wm" "skinCluster1.ma[6]";
connectAttr "Crw_Spine.wm" "skinCluster1.ma[11]";
connectAttr "Crw_Spine1.wm" "skinCluster1.ma[12]";
connectAttr "Crw_Spine2.wm" "skinCluster1.ma[13]";
connectAttr "Crw_Spine3.wm" "skinCluster1.ma[14]";
connectAttr "Crw_Neck.wm" "skinCluster1.ma[15]";
connectAttr "Crw_Head.wm" "skinCluster1.ma[16]";
connectAttr "Crw_LeftShoulder.wm" "skinCluster1.ma[18]";
connectAttr "Crw_LeftArm.wm" "skinCluster1.ma[19]";
connectAttr "Crw_LeftForeArm.wm" "skinCluster1.ma[20]";
connectAttr "Crw_RightShoulder.wm" "skinCluster1.ma[24]";
connectAttr "Crw_RightArm.wm" "skinCluster1.ma[25]";
connectAttr "Crw_RightForeArm.wm" "skinCluster1.ma[26]";
connectAttr "Crw_Hips.liw" "skinCluster1.lw[0]";
connectAttr "Crw_LeftUpLeg.liw" "skinCluster1.lw[1]";
connectAttr "Crw_RightUpLeg.liw" "skinCluster1.lw[6]";
connectAttr "Crw_Spine.liw" "skinCluster1.lw[11]";
connectAttr "Crw_Spine1.liw" "skinCluster1.lw[12]";
connectAttr "Crw_Spine2.liw" "skinCluster1.lw[13]";
connectAttr "Crw_Spine3.liw" "skinCluster1.lw[14]";
connectAttr "Crw_Neck.liw" "skinCluster1.lw[15]";
connectAttr "Crw_Head.liw" "skinCluster1.lw[16]";
connectAttr "Crw_LeftShoulder.liw" "skinCluster1.lw[18]";
connectAttr "Crw_LeftArm.liw" "skinCluster1.lw[19]";
connectAttr "Crw_LeftForeArm.liw" "skinCluster1.lw[20]";
connectAttr "Crw_RightShoulder.liw" "skinCluster1.lw[24]";
connectAttr "Crw_RightArm.liw" "skinCluster1.lw[25]";
connectAttr "Crw_RightForeArm.liw" "skinCluster1.lw[26]";
connectAttr "bindPose1.msg" "skinCluster1.bp";
connectAttr "Crw_RightArm.msg" "skinCluster1.ptt";
connectAttr "groupParts2.og" "tweak1.ip[0].ig";
connectAttr "groupId2.id" "tweak1.ip[0].gi";
connectAttr "skinCluster1GroupId.msg" "skinCluster1Set.gn" -na;
connectAttr "mocap_shirt_PLYShape.iog.og[0]" "skinCluster1Set.dsm" -na;
connectAttr "skinCluster1.msg" "skinCluster1Set.ub[0]";
connectAttr "tweak1.og[0]" "skinCluster1GroupParts.ig";
connectAttr "skinCluster1GroupId.id" "skinCluster1GroupParts.gi";
connectAttr "groupId2.msg" "tweakSet1.gn" -na;
connectAttr "mocap_shirt_PLYShape.iog.og[1]" "tweakSet1.dsm" -na;
connectAttr "tweak1.msg" "tweakSet1.ub[0]";
connectAttr "mocap_shirt_PLYShapeOrig.w" "groupParts2.ig";
connectAttr "groupId2.id" "groupParts2.gi";
connectAttr "skinCluster2GroupParts.og" "skinCluster2.ip[0].ig";
connectAttr "skinCluster2GroupId.id" "skinCluster2.ip[0].gi";
connectAttr "Crw_Spine2.wm" "skinCluster2.ma[13]";
connectAttr "Crw_Spine3.wm" "skinCluster2.ma[14]";
connectAttr "Crw_Neck.wm" "skinCluster2.ma[15]";
connectAttr "Crw_Head.wm" "skinCluster2.ma[16]";
connectAttr "Crw_Hair.wm" "skinCluster2.ma[17]";
connectAttr "Crw_LeftShoulder.wm" "skinCluster2.ma[18]";
connectAttr "Crw_LeftArm.wm" "skinCluster2.ma[19]";
connectAttr "Crw_RightShoulder.wm" "skinCluster2.ma[24]";
connectAttr "Crw_RightArm.wm" "skinCluster2.ma[25]";
connectAttr "Crw_hairTip.wm" "skinCluster2.ma[27]";
connectAttr "Crw_Spine2.liw" "skinCluster2.lw[13]";
connectAttr "Crw_Spine3.liw" "skinCluster2.lw[14]";
connectAttr "Crw_Neck.liw" "skinCluster2.lw[15]";
connectAttr "Crw_Head.liw" "skinCluster2.lw[16]";
connectAttr "Crw_Hair.liw" "skinCluster2.lw[17]";
connectAttr "Crw_LeftShoulder.liw" "skinCluster2.lw[18]";
connectAttr "Crw_LeftArm.liw" "skinCluster2.lw[19]";
connectAttr "Crw_RightShoulder.liw" "skinCluster2.lw[24]";
connectAttr "Crw_RightArm.liw" "skinCluster2.lw[25]";
connectAttr "Crw_hairTip.liw" "skinCluster2.lw[27]";
connectAttr "bindPose1.msg" "skinCluster2.bp";
connectAttr "Crw_Head.msg" "skinCluster2.ptt";
connectAttr "Crw_hairTip.obcc" "skinCluster2.ifcl[27]";
connectAttr "groupParts4.og" "tweak2.ip[0].ig";
connectAttr "groupId4.id" "tweak2.ip[0].gi";
connectAttr "skinCluster2GroupId.msg" "skinCluster2Set.gn" -na;
connectAttr "mocap_head_PLYShape.iog.og[0]" "skinCluster2Set.dsm" -na;
connectAttr "skinCluster2.msg" "skinCluster2Set.ub[0]";
connectAttr "tweak2.og[0]" "skinCluster2GroupParts.ig";
connectAttr "skinCluster2GroupId.id" "skinCluster2GroupParts.gi";
connectAttr "groupId4.msg" "tweakSet2.gn" -na;
connectAttr "mocap_head_PLYShape.iog.og[1]" "tweakSet2.dsm" -na;
connectAttr "tweak2.msg" "tweakSet2.ub[0]";
connectAttr "mocap_head_PLYShapeOrig.w" "groupParts4.ig";
connectAttr "groupId4.id" "groupParts4.gi";
connectAttr "skinCluster3GroupParts.og" "skinCluster3.ip[0].ig";
connectAttr "skinCluster3GroupId.id" "skinCluster3.ip[0].gi";
connectAttr "Crw_Spine2.wm" "skinCluster3.ma[13]";
connectAttr "Crw_Spine3.wm" "skinCluster3.ma[14]";
connectAttr "Crw_Neck.wm" "skinCluster3.ma[15]";
connectAttr "Crw_LeftShoulder.wm" "skinCluster3.ma[18]";
connectAttr "Crw_LeftArm.wm" "skinCluster3.ma[19]";
connectAttr "Crw_LeftForeArm.wm" "skinCluster3.ma[20]";
connectAttr "Crw_LeftHand.wm" "skinCluster3.ma[21]";
connectAttr "Crw_LefthandSub1.wm" "skinCluster3.ma[22]";
connectAttr "Crw_LefthandSub2.wm" "skinCluster3.ma[23]";
connectAttr "Crw_RightShoulder.wm" "skinCluster3.ma[24]";
connectAttr "Crw_RightArm.wm" "skinCluster3.ma[25]";
connectAttr "Crw_RightForeArm.wm" "skinCluster3.ma[26]";
connectAttr "Crw_RightHand.wm" "skinCluster3.ma[27]";
connectAttr "Crw_RightHandSub1.wm" "skinCluster3.ma[28]";
connectAttr "Crw_RightHandSub2.wm" "skinCluster3.ma[29]";
connectAttr "Crw_Spine2.liw" "skinCluster3.lw[13]";
connectAttr "Crw_Spine3.liw" "skinCluster3.lw[14]";
connectAttr "Crw_Neck.liw" "skinCluster3.lw[15]";
connectAttr "Crw_LeftShoulder.liw" "skinCluster3.lw[18]";
connectAttr "Crw_LeftArm.liw" "skinCluster3.lw[19]";
connectAttr "Crw_LeftForeArm.liw" "skinCluster3.lw[20]";
connectAttr "Crw_LeftHand.liw" "skinCluster3.lw[21]";
connectAttr "Crw_LefthandSub1.liw" "skinCluster3.lw[22]";
connectAttr "Crw_LefthandSub2.liw" "skinCluster3.lw[23]";
connectAttr "Crw_RightShoulder.liw" "skinCluster3.lw[24]";
connectAttr "Crw_RightArm.liw" "skinCluster3.lw[25]";
connectAttr "Crw_RightForeArm.liw" "skinCluster3.lw[26]";
connectAttr "Crw_RightHand.liw" "skinCluster3.lw[27]";
connectAttr "Crw_RightHandSub1.liw" "skinCluster3.lw[28]";
connectAttr "Crw_RightHandSub2.liw" "skinCluster3.lw[29]";
connectAttr "bindPose1.msg" "skinCluster3.bp";
connectAttr "Crw_LefthandSub1.msg" "skinCluster3.ptt";
connectAttr "groupParts6.og" "tweak3.ip[0].ig";
connectAttr "groupId6.id" "tweak3.ip[0].gi";
connectAttr "skinCluster3GroupId.msg" "skinCluster3Set.gn" -na;
connectAttr "mocap_arm_PLYShape.iog.og[0]" "skinCluster3Set.dsm" -na;
connectAttr "skinCluster3.msg" "skinCluster3Set.ub[0]";
connectAttr "tweak3.og[0]" "skinCluster3GroupParts.ig";
connectAttr "skinCluster3GroupId.id" "skinCluster3GroupParts.gi";
connectAttr "groupId6.msg" "tweakSet3.gn" -na;
connectAttr "mocap_arm_PLYShape.iog.og[1]" "tweakSet3.dsm" -na;
connectAttr "tweak3.msg" "tweakSet3.ub[0]";
connectAttr "mocap_arm_PLYShapeOrig.w" "groupParts6.ig";
connectAttr "groupId6.id" "groupParts6.gi";
connectAttr "skinCluster4GroupParts.og" "skinCluster4.ip[0].ig";
connectAttr "skinCluster4GroupId.id" "skinCluster4.ip[0].gi";
connectAttr "Crw_Hips.wm" "skinCluster4.ma[0]";
connectAttr "Crw_LeftUpLeg.wm" "skinCluster4.ma[1]";
connectAttr "Crw_LeftLeg.wm" "skinCluster4.ma[2]";
connectAttr "Crw_LeftFoot.wm" "skinCluster4.ma[3]";
connectAttr "Crw_LeftToeBase.wm" "skinCluster4.ma[4]";
connectAttr "Crw_LeftToe.wm" "skinCluster4.ma[5]";
connectAttr "Crw_RightUpLeg.wm" "skinCluster4.ma[6]";
connectAttr "Crw_RightLeg.wm" "skinCluster4.ma[7]";
connectAttr "Crw_RightFoot.wm" "skinCluster4.ma[8]";
connectAttr "Crw_RightToeBase.wm" "skinCluster4.ma[9]";
connectAttr "Crw_RightToe.wm" "skinCluster4.ma[10]";
connectAttr "Crw_Spine.wm" "skinCluster4.ma[11]";
connectAttr "Crw_Spine1.wm" "skinCluster4.ma[12]";
connectAttr "Crw_Hips.liw" "skinCluster4.lw[0]";
connectAttr "Crw_LeftUpLeg.liw" "skinCluster4.lw[1]";
connectAttr "Crw_LeftLeg.liw" "skinCluster4.lw[2]";
connectAttr "Crw_LeftFoot.liw" "skinCluster4.lw[3]";
connectAttr "Crw_LeftToeBase.liw" "skinCluster4.lw[4]";
connectAttr "Crw_LeftToe.liw" "skinCluster4.lw[5]";
connectAttr "Crw_RightUpLeg.liw" "skinCluster4.lw[6]";
connectAttr "Crw_RightLeg.liw" "skinCluster4.lw[7]";
connectAttr "Crw_RightFoot.liw" "skinCluster4.lw[8]";
connectAttr "Crw_RightToeBase.liw" "skinCluster4.lw[9]";
connectAttr "Crw_RightToe.liw" "skinCluster4.lw[10]";
connectAttr "Crw_Spine.liw" "skinCluster4.lw[11]";
connectAttr "Crw_Spine1.liw" "skinCluster4.lw[12]";
connectAttr "bindPose1.msg" "skinCluster4.bp";
connectAttr "Crw_RightUpLeg.msg" "skinCluster4.ptt";
connectAttr "groupParts8.og" "tweak4.ip[0].ig";
connectAttr "groupId8.id" "tweak4.ip[0].gi";
connectAttr "skinCluster4GroupId.msg" "skinCluster4Set.gn" -na;
connectAttr "mocap_pant_PLYShape.iog.og[0]" "skinCluster4Set.dsm" -na;
connectAttr "skinCluster4.msg" "skinCluster4Set.ub[0]";
connectAttr "tweak4.og[0]" "skinCluster4GroupParts.ig";
connectAttr "skinCluster4GroupId.id" "skinCluster4GroupParts.gi";
connectAttr "groupId8.msg" "tweakSet4.gn" -na;
connectAttr "mocap_pant_PLYShape.iog.og[1]" "tweakSet4.dsm" -na;
connectAttr "tweak4.msg" "tweakSet4.ub[0]";
connectAttr "mocap_pant_PLYShapeOrig.w" "groupParts8.ig";
connectAttr "groupId8.id" "groupParts8.gi";
connectAttr "skinCluster5GroupParts.og" "skinCluster5.ip[0].ig";
connectAttr "skinCluster5GroupId.id" "skinCluster5.ip[0].gi";
connectAttr "Crw_LeftLeg.wm" "skinCluster5.ma[2]";
connectAttr "Crw_LeftFoot.wm" "skinCluster5.ma[3]";
connectAttr "Crw_LeftToeBase.wm" "skinCluster5.ma[4]";
connectAttr "Crw_LeftToe.wm" "skinCluster5.ma[5]";
connectAttr "Crw_RightLeg.wm" "skinCluster5.ma[7]";
connectAttr "Crw_RightFoot.wm" "skinCluster5.ma[8]";
connectAttr "Crw_RightToeBase.wm" "skinCluster5.ma[9]";
connectAttr "Crw_RightToe.wm" "skinCluster5.ma[10]";
connectAttr "Crw_LeftLeg.liw" "skinCluster5.lw[2]";
connectAttr "Crw_LeftFoot.liw" "skinCluster5.lw[3]";
connectAttr "Crw_LeftToeBase.liw" "skinCluster5.lw[4]";
connectAttr "Crw_LeftToe.liw" "skinCluster5.lw[5]";
connectAttr "Crw_RightLeg.liw" "skinCluster5.lw[7]";
connectAttr "Crw_RightFoot.liw" "skinCluster5.lw[8]";
connectAttr "Crw_RightToeBase.liw" "skinCluster5.lw[9]";
connectAttr "Crw_RightToe.liw" "skinCluster5.lw[10]";
connectAttr "bindPose1.msg" "skinCluster5.bp";
connectAttr "Crw_LeftToeBase.msg" "skinCluster5.ptt";
connectAttr "groupParts10.og" "tweak5.ip[0].ig";
connectAttr "groupId10.id" "tweak5.ip[0].gi";
connectAttr "skinCluster5GroupId.msg" "skinCluster5Set.gn" -na;
connectAttr "mocap_shoe_L_PLYShape.iog.og[0]" "skinCluster5Set.dsm" -na;
connectAttr "skinCluster5.msg" "skinCluster5Set.ub[0]";
connectAttr "tweak5.og[0]" "skinCluster5GroupParts.ig";
connectAttr "skinCluster5GroupId.id" "skinCluster5GroupParts.gi";
connectAttr "groupId10.msg" "tweakSet5.gn" -na;
connectAttr "mocap_shoe_L_PLYShape.iog.og[1]" "tweakSet5.dsm" -na;
connectAttr "tweak5.msg" "tweakSet5.ub[0]";
connectAttr "mocap_shoe_L_PLYShapeOrig.w" "groupParts10.ig";
connectAttr "groupId10.id" "groupParts10.gi";
connectAttr "skinCluster6GroupParts.og" "skinCluster6.ip[0].ig";
connectAttr "skinCluster6GroupId.id" "skinCluster6.ip[0].gi";
connectAttr "Crw_LeftLeg.wm" "skinCluster6.ma[2]";
connectAttr "Crw_LeftFoot.wm" "skinCluster6.ma[3]";
connectAttr "Crw_LeftToeBase.wm" "skinCluster6.ma[4]";
connectAttr "Crw_LeftToe.wm" "skinCluster6.ma[5]";
connectAttr "Crw_RightLeg.wm" "skinCluster6.ma[7]";
connectAttr "Crw_RightFoot.wm" "skinCluster6.ma[8]";
connectAttr "Crw_RightToeBase.wm" "skinCluster6.ma[9]";
connectAttr "Crw_RightToe.wm" "skinCluster6.ma[10]";
connectAttr "Crw_LeftLeg.liw" "skinCluster6.lw[2]";
connectAttr "Crw_LeftFoot.liw" "skinCluster6.lw[3]";
connectAttr "Crw_LeftToeBase.liw" "skinCluster6.lw[4]";
connectAttr "Crw_LeftToe.liw" "skinCluster6.lw[5]";
connectAttr "Crw_RightLeg.liw" "skinCluster6.lw[7]";
connectAttr "Crw_RightFoot.liw" "skinCluster6.lw[8]";
connectAttr "Crw_RightToeBase.liw" "skinCluster6.lw[9]";
connectAttr "Crw_RightToe.liw" "skinCluster6.lw[10]";
connectAttr "bindPose1.msg" "skinCluster6.bp";
connectAttr "Crw_RightFoot.msg" "skinCluster6.ptt";
connectAttr "groupParts12.og" "tweak6.ip[0].ig";
connectAttr "groupId12.id" "tweak6.ip[0].gi";
connectAttr "skinCluster6GroupId.msg" "skinCluster6Set.gn" -na;
connectAttr "mocap_shoe_R_PLYShape.iog.og[0]" "skinCluster6Set.dsm" -na;
connectAttr "skinCluster6.msg" "skinCluster6Set.ub[0]";
connectAttr "tweak6.og[0]" "skinCluster6GroupParts.ig";
connectAttr "skinCluster6GroupId.id" "skinCluster6GroupParts.gi";
connectAttr "groupId12.msg" "tweakSet6.gn" -na;
connectAttr "mocap_shoe_R_PLYShape.iog.og[1]" "tweakSet6.dsm" -na;
connectAttr "tweak6.msg" "tweakSet6.ub[0]";
connectAttr "mocap_shoe_R_PLYShapeOrig.w" "groupParts12.ig";
connectAttr "groupId12.id" "groupParts12.gi";
connectAttr ":defaultRenderGlobals.msg" "mtorPartition.rgcnx";
connectAttr "lambert3.oc" "lambert3SG.ss";
connectAttr "mocap_shoe_R_PLYShape.iog" "lambert3SG.dsm" -na;
connectAttr "mocap_shoe_L_PLYShape.iog" "lambert3SG.dsm" -na;
connectAttr "mocap_pant_PLYShape.iog" "lambert3SG.dsm" -na;
connectAttr "mocap_arm_PLYShape.iog" "lambert3SG.dsm" -na;
connectAttr "mocap_head_PLYShape.iog" "lambert3SG.dsm" -na;
connectAttr "mocap_shirt_PLYShape.iog" "lambert3SG.dsm" -na;
connectAttr "lambert3SG.msg" "materialInfo2.sg";
connectAttr "lambert3.msg" "materialInfo2.m";
connectAttr "HIKproperties1.msg" "Character1.propertyState";
connectAttr "Crw_Head.ch" "Character1.Head";
connectAttr "Crw_Hips.ch" "Character1.Hips";
connectAttr "Crw_LeftArm.ch" "Character1.LeftArm";
connectAttr "Crw_LeftFoot.ch" "Character1.LeftFoot";
connectAttr "Crw_LeftForeArm.ch" "Character1.LeftForeArm";
connectAttr "Crw_LeftHand.ch" "Character1.LeftHand";
connectAttr "Crw_LeftLeg.ch" "Character1.LeftLeg";
connectAttr "Crw_LeftShoulder.ch" "Character1.LeftShoulder";
connectAttr "Crw_LeftToeBase.ch" "Character1.LeftToeBase";
connectAttr "Crw_LeftUpLeg.ch" "Character1.LeftUpLeg";
connectAttr "Crw_Neck.ch" "Character1.Neck";
connectAttr "Crw_RightArm.ch" "Character1.RightArm";
connectAttr "Crw_RightFoot.ch" "Character1.RightFoot";
connectAttr "Crw_RightForeArm.ch" "Character1.RightForeArm";
connectAttr "Crw_RightHand.ch" "Character1.RightHand";
connectAttr "Crw_RightLeg.ch" "Character1.RightLeg";
connectAttr "Crw_RightShoulder.ch" "Character1.RightShoulder";
connectAttr "Crw_RightToeBase.ch" "Character1.RightToeBase";
connectAttr "Crw_RightUpLeg.ch" "Character1.RightUpLeg";
connectAttr "Crw_Spine.ch" "Character1.Spine";
connectAttr "Crw_Spine1.ch" "Character1.Spine1";
connectAttr "Crw_Spine2.ch" "Character1.Spine2";
connectAttr "mocap_char_GRP.msg" "nodeGraphEditorBookmarkInfo1.ni[0].dn";
connectAttr "lambert2SG.pa" ":renderPartition.st" -na;
connectAttr "initialShadingGroup1.pa" ":renderPartition.st" -na;
connectAttr "lambert2SG1.pa" ":renderPartition.st" -na;
connectAttr "initialShadingGroup2.pa" ":renderPartition.st" -na;
connectAttr "lambert2SG2.pa" ":renderPartition.st" -na;
connectAttr "initialShadingGroup3.pa" ":renderPartition.st" -na;
connectAttr "lambert3SG.pa" ":renderPartition.st" -na;
connectAttr "lambert3.msg" ":defaultShaderList1.s" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr ":perspShape.msg" ":defaultRenderGlobals.sc";
// End of HIKJoint_2018.08.06.ma
