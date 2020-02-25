//Maya ASCII 2014 scene
//Name: arm_template.ma
//Last modified: Sun, Jan 10, 2016 02:14:28 PM
//Codeset: 949
requires maya "2014";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2014";
fileInfo "version" "2014 x64";
fileInfo "cutIdentifier" "201303010241-864206";
fileInfo "osv" "Microsoft Windows 8 Business Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	setAttr ".t" -type "double3" 4.2167998492752456 19.13446383130734 10.932542920370315 ;
	setAttr ".r" -type "double3" 300.8616472703398 42.599999999900064 359.99999999998477 ;
	setAttr ".rp" -type "double3" 1.4210854715202004e-014 6.6613381477509392e-015 0 ;
	setAttr ".rpt" -type "double3" 1.8170116107083013e-016 -5.9200902575159532e-016 
		1.5295087487412179e-015 ;
createNode camera -s -n "perspShape" -p "persp";
	setAttr -k off ".v";
	setAttr ".fl" 34.999999999999979;
	setAttr ".coi" 23.091457027040033;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 0.30000000000000004 0 1 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	setAttr ".t" -type "double3" 0 100.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	setAttr -k off ".v";
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	setAttr ".t" -type "double3" 0 0 100.1 ;
createNode camera -s -n "frontShape" -p "front";
	setAttr -k off ".v";
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	setAttr ".t" -type "double3" 100.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	setAttr -k off ".v";
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "arm_system";
createNode transform -n "init" -p "arm_system";
createNode transform -n "clavicle_init" -p "init";
	setAttr ".t" -type "double3" 0.3 0 1 ;
	setAttr ".r" -type "double3" 0 261.46923439005189 0 ;
createNode transform -n "clavicle_align" -p "init";
	setAttr ".t" -type "double3" 0.3 0 1 ;
	setAttr ".r" -type "double3" 0 257.77487732426425 0 ;
createNode transform -n "uparm_align" -p "clavicle_align";
	setAttr ".t" -type "double3" 2.0223748416156684 0 -3.3306690738754696e-016 ;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
createNode transform -n "uparm_init" -p "init";
	setAttr ".t" -type "double3" 0 0 3 ;
	setAttr ".r" -type "double3" 0 255.96375653207352 0 ;
createNode transform -n "loarm_init" -p "init";
	setAttr ".t" -type "double3" -0.99999999999999989 0 7 ;
	setAttr ".r" -type "double3" 0 -75.963756532073532 0 ;
createNode transform -n "loarm_up" -p "loarm_init";
	setAttr ".t" -type "double3" 1.7763568394002501e-015 1 0 ;
createNode transform -n "wrist_init" -p "init";
	setAttr ".t" -type "double3" -1.1102230246251563e-016 0 11 ;
	setAttr ".r" -type "double3" 0 -75.963756532073532 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1 ;
createNode transform -n "pole_init" -p "init";
	setAttr ".t" -type "double3" -6 0 7.0000000000000009 ;
createNode transform -n "motion_input" -p "arm_system";
createNode transform -n "clavicle_placement" -p "motion_input";
	setAttr ".t" -type "double3" 0.3 0 1 ;
	setAttr ".r" -type "double3" 0 261.46923439005189 0 ;
createNode transform -n "clavicle_child_plug" -p "clavicle_placement";
	setAttr ".t" -type "double3" 7.7715611723760978e-016 0 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1.0000000000000002 ;
createNode transform -n "wrist_placement" -p "motion_input";
	setAttr ".t" -type "double3" -1.1102230246251563e-016 0 11 ;
	setAttr ".r" -type "double3" 0 -75.963756532073532 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1 ;
createNode transform -n "wrist_child_plug" -p "wrist_placement";
	setAttr ".t" -type "double3" -1.7763568394002686e-015 0 0 ;
	setAttr ".s" -type "double3" 1 0.99999999999999989 0.99999999999999989 ;
createNode transform -n "uparm_placement" -p "motion_input";
	setAttr ".t" -type "double3" 0 0 3 ;
	setAttr ".r" -type "double3" 0 255.96375653207352 0 ;
createNode transform -n "uparm_child_plug" -p "uparm_placement";
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
createNode transform -n "pole_placement" -p "motion_input";
	setAttr ".t" -type "double3" -6 0 7.0000000000000009 ;
createNode locator -n "pole_placementShape" -p "pole_placement";
	setAttr -k off ".v";
createNode transform -n "pole_child_plug" -p "pole_placement";
createNode locator -n "pole_child_plugShape" -p "pole_child_plug";
	setAttr -k off ".v";
createNode transform -n "motion_fk" -p "arm_system";
	setAttr ".v" no;
createNode transform -n "arm_fk_placement" -p "motion_fk";
	setAttr ".t" -type "double3" 0.3 0 1 ;
	setAttr ".r" -type "double3" 0 261.46923439005189 0 ;
createNode transform -n "arm_fk_space" -p "arm_fk_placement";
	setAttr ".t" -type "double3" 7.7715611723760978e-016 0 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1.0000000000000002 ;
createNode joint -n "clavicle_fk_jnt" -p "arm_fk_space";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
	setAttr ".radi" 0.55288145732494831;
createNode joint -n "uparm_fk_jnt" -p "clavicle_fk_jnt";
	setAttr ".t" -type "double3" 2.0223748416156684 0 -3.3306690738754696e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -5.5054778579783541 0 ;
	setAttr ".radi" 0.66153994615263767;
createNode joint -n "loarm_fk_jnt" -p "uparm_fk_jnt";
	setAttr ".t" -type "double3" 4.1231056256176597 0 -1.3322676295501878e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 28.072486935852968 0 ;
	setAttr ".radi" 0.66153994615263767;
createNode joint -n "wrist_fk_jnt" -p "loarm_fk_jnt";
	setAttr ".t" -type "double3" 4.1231056256176624 0 0 ;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.66153994615263756;
createNode transform -n "motion_ik" -p "arm_system";
	addAttr -ci true -sn "useAutoShldr" -ln "useAutoShldr" -nn "Use Auto Shldr" -min 
		0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr -k on ".useAutoShldr" yes;
createNode transform -n "arm_basis_ik_placement" -p "motion_ik";
	setAttr ".t" -type "double3" 0.3 0 1 ;
	setAttr ".r" -type "double3" 0 261.46923439005189 0 ;
createNode transform -n "arm_basis_ik_space" -p "arm_basis_ik_placement";
	setAttr ".t" -type "double3" 7.7715611723760978e-016 0 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1.0000000000000002 ;
createNode transform -n "uparm_base_ik_parent_space" -p "arm_basis_ik_space";
	setAttr ".t" -type "double3" 2.0223748416156684 0 -3.3306690738754696e-016 ;
	setAttr ".r" -type "double3" 0 -5.5054778579783541 0 ;
createNode transform -n "uparm_basis_ik_space" -p "uparm_base_ik_parent_space";
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
createNode joint -n "uparm_basis_ik_jnt" -p "uparm_basis_ik_space";
	setAttr ".r" -type "double3" -1.2273598990643173e-006 3.2864818635708453e-015 3.0683997476608256e-007 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 3.1805546814635176e-015 0 ;
	setAttr ".pa" -type "double3" -1.9953889285859233e-007 8.6864534573051917e-017 4.9884723214648082e-008 ;
	setAttr ".radi" 0.66153994615263767;
createNode joint -n "loarm_basis_ik_jnt" -p "uparm_basis_ik_jnt";
	setAttr ".t" -type "double3" 4.1231056256176597 0 -1.3322676295501878e-015 ;
	setAttr ".r" -type "double3" 1.0692873410961308e-053 2.3908394933832502e-013 1.4039913354761441e-037 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 28.072486935852968 0 ;
	setAttr ".pa" -type "double3" 0 -1.994668925268561e-013 0 ;
	setAttr ".radi" 0.66153994615263767;
createNode joint -n "wrist_basis_ik_jnt" -p "loarm_basis_ik_jnt";
	setAttr ".t" -type "double3" 4.1231056256176624 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.66153994615263756;
createNode ikEffector -n "effector1" -p "loarm_basis_ik_jnt";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode transform -n "loarm_basis_ik_jnt_ref" -p "loarm_basis_ik_jnt";
createNode transform -n "uparm_basis_ik_jnt_ref" -p "uparm_basis_ik_jnt";
createNode transform -n "uparm_basis_ik_soft_space" -p "uparm_basis_ik_space";
	setAttr ".r" -type "double3" -1.3442397078560253e-031 14.036243467926434 -1.0919401133063956e-030 ;
createNode transform -n "uparm_basis_ik_soft" -p "uparm_basis_ik_soft_space";
	setAttr ".t" -type "double3" 8 0 0 ;
createNode transform -n "arm_basis_ik_handle_space" -p "arm_basis_ik_space";
	setAttr ".t" -type "double3" 9.9338656645620436 0 -1.1867236234419485 ;
	setAttr ".r" -type "double3" 0 22.567009077874559 0 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999933 ;
createNode ikHandle -n "arm_basis_ik_handle" -p "arm_basis_ik_handle_space";
	setAttr ".roc" yes;
createNode poleVectorConstraint -n "arm_basis_ikHandle_poleVectorConstraint1" -p "arm_basis_ik_handle";
	addAttr -ci true -k true -sn "w0" -ln "arm_poleVecCon_ik_refW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 2.9104275004359952 0 4.8507125007266598 ;
	setAttr -k on ".w0";
createNode transform -n "arm_ik_placement" -p "motion_ik";
	setAttr ".t" -type "double3" 0.3 0 1 ;
	setAttr ".r" -type "double3" 0 261.46923439005189 0 ;
createNode transform -n "arm_ik_space" -p "arm_ik_placement";
	setAttr ".t" -type "double3" 7.7715611723760978e-016 0 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1.0000000000000002 ;
createNode joint -n "clavicle_ik_jnt" -p "arm_ik_space";
	setAttr ".t" -type "double3" -3.3306690738754696e-016 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
	setAttr ".radi" 0.55288145732494831;
createNode joint -n "uparm_ik_jnt" -p "clavicle_ik_jnt";
	setAttr ".t" -type "double3" 2.0223748416156684 0 -3.3306690738754696e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -5.5054778579783541 0 ;
	setAttr ".radi" 0.66153994615263767;
createNode joint -n "loarm_ik_jnt" -p "uparm_ik_jnt";
	setAttr ".t" -type "double3" 4.1231056256176597 0 -1.3322676295501878e-015 ;
	setAttr ".r" -type "double3" 0 -2.9735505066166083e-006 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 28.072486935852968 0 ;
	setAttr ".radi" 0.66153994615263767;
createNode joint -n "wrist_ik_jnt" -p "loarm_ik_jnt";
	setAttr ".t" -type "double3" 4.1231056256176624 0 0 ;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.66153994615263756;
createNode ikEffector -n "effector4" -p "loarm_ik_jnt";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode ikEffector -n "effector3" -p "clavicle_ik_jnt";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode transform -n "uparm_ik_soft_space" -p "arm_ik_space";
	setAttr ".t" -type "double3" 2.0223748683929443 0 -2.7755575615628914e-016 ;
	setAttr ".r" -type "double3" -7.989226380740196e-032 8.5307656383964989 -1.0711887696766233e-030 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
createNode transform -n "uparm_ik_soft" -p "uparm_ik_soft_space";
	setAttr ".t" -type "double3" 8 0 0 ;
createNode transform -n "arm_ik_handle_space" -p "arm_ik_space";
	setAttr ".t" -type "double3" 9.9338656645620436 0 -1.1867236234419485 ;
	setAttr ".r" -type "double3" 0 22.567009077874559 0 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999933 ;
createNode ikHandle -n "arm_ik_handle" -p "arm_ik_handle_space";
	setAttr ".t" -type "double3" 2.5690370719644307e-008 0 6.4225971208031751e-009 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
	setAttr ".roc" yes;
createNode poleVectorConstraint -n "arm_ik_handle_poleVectorConstraint1" -p "arm_ik_handle";
	addAttr -ci true -k true -sn "w0" -ln "arm_poleVecCon_ik_refW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 2.9104275004359943 0 4.8507125007266589 ;
	setAttr -k on ".w0";
createNode transform -n "shldr_ik_handle_space" -p "arm_ik_space";
	setAttr ".t" -type "double3" 2.0223748416156684 0 -3.3306690738754696e-016 ;
	setAttr ".r" -type "double3" 0 -5.5054778579783541 0 ;
createNode ikHandle -n "shldr_ik_handle" -p "shldr_ik_handle_space";
	setAttr ".t" -type "double3" 2.6653752538408071e-008 0 -2.5690358729235641e-009 ;
	setAttr ".roc" yes;
createNode poleVectorConstraint -n "shldr_ik_handle_poleVectorConstraint1" -p "shldr_ik_handle";
	addAttr -ci true -k true -sn "w0" -ln "arm_pole_ik_Con_refW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 7.3488294386008883 0 4.6566840006975889 ;
	setAttr -k on ".w0";
createNode transform -n "arm_auto_ik_placement" -p "motion_ik";
	setAttr ".t" -type "double3" 0.3 0 1 ;
	setAttr ".r" -type "double3" 0 261.46923439005189 0 ;
createNode transform -n "arm_auto_ik_space" -p "arm_auto_ik_placement";
	setAttr ".t" -type "double3" 7.7715611723760978e-016 0 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1.0000000000000002 ;
createNode joint -n "clavicle_auto_ik_jnt" -p "arm_auto_ik_space";
	setAttr ".r" -type "double3" 0 -3.6943570657875688 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.55288145732494831;
createNode joint -n "uparm_auto_ik_jnt" -p "clavicle_auto_ik_jnt";
	setAttr ".t" -type "double3" 2.0223748416156684 0 -3.3306690738754696e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.55288145732494831;
createNode transform -n "uparm_auto_ik_space" -p "uparm_auto_ik_jnt";
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
createNode transform -n "uparm_auto_ik_offset_space" -p "uparm_auto_ik_space";
	setAttr ".t" -type "double3" -0.0042025574603319349 0 -0.13030975200357331 ;
	setAttr ".r" -type "double3" 0 -1.8111207921907255 0 ;
createNode ikEffector -n "effector2" -p "clavicle_auto_ik_jnt";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode transform -n "shldr_auto_ik_handle_space" -p "arm_auto_ik_space";
	setAttr ".t" -type "double3" 6.1264607060191016 0 0.39557454114731799 ;
	setAttr ".r" -type "double3" 0 22.567009077874612 0 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
createNode ikHandle -n "shldr_auto_ik_handle" -p "shldr_auto_ik_handle_space";
	setAttr ".t" -type "double3" -4.4408920985006262e-016 0 -1.6653345369377348e-016 ;
	setAttr ".roc" yes;
createNode poleVectorConstraint -n "shldr_auto_ik_handle_poleVectorConstraint1" -p
		 "shldr_auto_ik_handle";
	addAttr -ci true -k true -sn "w0" -ln "arm_pole_ik_Con_refW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 4.2928805631430951 0 7.567111501133585 ;
	setAttr -k on ".w0";
createNode transform -n "elbow_target_space" -p "arm_auto_ik_space";
createNode transform -n "elbow_target" -p "elbow_target_space";
	setAttr ".t" -type "double3" 6.1264607060191016 0 0.39557454114731799 ;
	setAttr ".r" -type "double3" 0 22.567009077874612 0 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
createNode transform -n "arm_refer_placement" -p "motion_ik";
	setAttr ".t" -type "double3" 0.3 0 1 ;
	setAttr ".r" -type "double3" 0 261.46923439005189 0 ;
createNode transform -n "arm_refer_space" -p "arm_refer_placement";
	setAttr ".t" -type "double3" 7.7715611723760978e-016 0 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1.0000000000000002 ;
createNode transform -n "uparm_non_auto_ref" -p "arm_refer_space";
	setAttr ".t" -type "double3" 2.0223748416156679 0 -2.7755575615628914e-016 ;
	setAttr ".r" -type "double3" 0 -5.5054778579783585 0 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
createNode transform -n "uparm_auto_ref" -p "arm_refer_space";
	setAttr ".t" -type "double3" 2.0223748416156688 0 -2.3314683517128287e-015 ;
	setAttr ".r" -type "double3" 0 -5.5054778579782937 0 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
createNode transform -n "uparm_auto_blend_ref" -p "arm_refer_space";
	setAttr ".t" -type "double3" 2.0223748683929443 0 -2.7755575615628914e-016 ;
	setAttr ".r" -type "double3" 0 -5.5054778224701861 0 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
createNode transform -n "motion_output" -p "arm_system";
createNode transform -n "arm_blend_placement" -p "motion_output";
	setAttr ".t" -type "double3" 0.3 0 1 ;
	setAttr ".r" -type "double3" 0 261.46923439005189 0 ;
createNode transform -n "arm_blend_space" -p "arm_blend_placement";
	setAttr ".t" -type "double3" 7.7715611723760978e-016 0 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1.0000000000000002 ;
createNode joint -n "clavicle_blend_jnt" -p "arm_blend_space";
	setAttr ".ove" yes;
	setAttr ".r" -type "double3" -2.0567998291869544e-007 6.0799678061788889e-032 3.387363898445131e-023 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.55288145732494831;
createNode joint -n "uparm_blend_jnt" -p "clavicle_blend_jnt";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 2.0223748416156684 0 -3.3306690738754696e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -5.5054778579783541 0 ;
	setAttr ".radi" 0.66153994615263767;
createNode joint -n "loarm_blend_jnt" -p "uparm_blend_jnt";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 4.1231056256176597 0 -1.3322676295501878e-015 ;
	setAttr ".r" -type "double3" 0 -1.4867751705099486e-006 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 28.072486935852968 0 ;
	setAttr ".radi" 0.66153994615263767;
createNode joint -n "wrist_blend_jnt" -p "loarm_blend_jnt";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 4.1231056256176624 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.66153994615263756;
createNode transform -n "wrist_orbit_ref_space" -p "loarm_blend_jnt";
	setAttr ".t" -type "double3" 4.1231056256176624 0 0 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
createNode transform -n "wrist_orbit_ref" -p "wrist_orbit_ref_space";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr ".s" -type "double3" 1.0000000000000002 1 1.0000000000000002 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode joint -n "wrist_orbit_jnt" -p "wrist_orbit_ref";
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 0 -4.4408920985006262e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode transform -n "motion_control" -p "arm_system";
createNode transform -n "wrist_orbit_space" -p "motion_control";
	setAttr ".t" -type "double3" -2.0759296759376156e-007 0 11.000000051898244 ;
	setAttr ".r" -type "double3" 0 -75.963759505623813 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1.0000000000000002 ;
createNode transform -n "wrist_orbit_Con" -p "wrist_orbit_space";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr ".s" -type "double3" 0.99999999999999933 1 0.99999999999999933 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode nurbsCurve -n "wrist_orbit_ConShape" -p "wrist_orbit_Con";
	setAttr -k off ".v";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 0 no 3
		13 0 0 0 1 2 3 4 5 6 7 8 8 8
		11
		3.7493994566546433e-033 0.34202014332566871 -0.93969262078590843
		-1.3961795792256634e-017 0.55628267988784841 -0.86170743515890125
		-4.2812654152820829e-017 0.94118073461750784 -0.54159643063555019
		-6.536935339700164e-017 1.0675958317135821 0.18814865996277641
		-5.7522431009741912e-017 0.69728245660141353 0.83089085678602603
		-2.2713494181502702e-017 3.3306690738754696e-016 1.0845545716069869
		2.2720245605442947e-017 -0.69728245660141319 0.83089085678602603
		5.7488673890040563e-017 -1.0675958317135821 0.18814865996277683
		6.5497630451866712e-017 -0.9411807346175074 -0.54159643063554952
		5.0054745519330039e-017 -0.55628267988784863 -0.86170743515890047
		3.9359389436709919e-017 -0.34202014332566888 -0.93969262078590787
		;
createNode transform -n "arm_fk2ik_space" -p "motion_control";
	setAttr ".t" -type "double3" -2.0759296759376156e-007 0 11.000000051898244 ;
	setAttr ".r" -type "double3" 0 -75.963759505623813 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1.0000000000000002 ;
createNode transform -n "arm_fk2ik_Con" -p "arm_fk2ik_space";
	addAttr -ci true -sn "fk2ik" -ln "fk2ik" -nn "Fk2Ik" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "controlDisplay" -ln "controlDisplay" -nn "Control Display" 
		-min 0 -max 1 -en "FK:IK" -at "enum";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr ".s" -type "double3" 0.999999999999999 0.99999999999999989 1.0000000000000009 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr -k on ".fk2ik" 1;
	setAttr -k on ".controlDisplay" 1;
createNode nurbsCurve -n "arm_fk2ik_ConShape" -p "arm_fk2ik_Con";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		0 0 0
		0.49999911882979658 -4.4408920985006281e-016 2
		-0.49999911882978937 -4.4408920985006281e-016 2
		0 0 0
		3.7747578924073528e-015 0.4999999999999995 2
		3.7747578924073528e-015 -4.4408920985006281e-016 2
		3.7747578924073528e-015 -0.50000000000000044 2
		0 0 0
		;
createNode transform -n "ik_Con_placement" -p "motion_control";
	setAttr ".t" -type "double3" 0.3 0 1 ;
	setAttr ".r" -type "double3" 0 261.46923439005189 0 ;
createNode transform -n "ik_Con_space" -p "ik_Con_placement";
	setAttr ".t" -type "double3" 7.7715611723760978e-016 0 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1.0000000000000002 ;
createNode transform -n "wrist_ik_space" -p "ik_Con_space";
	setAttr ".t" -type "double3" 9.9338656645620436 0 -1.1867236234419485 ;
	setAttr ".r" -type "double3" 0 98.530765609948091 0 ;
	setAttr ".s" -type "double3" 0.99999999999999956 1 0.99999999999999956 ;
createNode transform -n "wrist_ik_Con" -p "wrist_ik_space";
	addAttr -ci true -sn "softIK" -ln "softIK" -nn "Soft IK" -dv 0.5 -min 0 -max 1 
		-at "double";
	addAttr -ci true -sn "autoShldr" -ln "autoShldr" -nn "Auto Shldr" -dv 0.5 -min 0 
		-max 1 -at "double";
	addAttr -ci true -sn "spaceUpbody2All" -ln "spaceUpbody2All" -nn "Space Upbody 2 All" 
		-min 0 -max 1 -at "double";
	addAttr -ci true -sn "spaceChest2Upbody" -ln "spaceChest2Upbody" -nn "Space Chest 2 Upbody" 
		-min 0 -max 1 -at "double";
	addAttr -ci true -sn "useConnection" -ln "useConnection" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 0 1.9721522630525365e-031 ;
	setAttr ".rp" -type "double3" 1.6145726800579152e-015 0 0 ;
	setAttr -k on ".softIK" 0;
	setAttr -k on ".autoShldr" 0;
	setAttr -k on ".spaceUpbody2All" 1;
	setAttr -k on ".spaceChest2Upbody";
	setAttr ".useConnection" yes;
createNode nurbsCurve -n "wrist_ik_ConShape" -p "wrist_ik_Con";
	setAttr -k off ".v";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-1 -1 1
		1 -1 1
		1 -1 -1
		-1 -1 -1
		-1 -1 1
		-1 1 1.0000000000000009
		-1 1 -1.0000000000000009
		-1 -1 -1.0000000000000009
		1 -1 -1
		1 1 -1.0000000000000009
		1.0000000000000009 1 1.0000000000000002
		1 -1 1
		-1 -1 1
		-1 1 1.0000000000000009
		1.0000000000000009 1 1.0000000000000002
		1 1 -1.0000000000000009
		-1 1 -1.0000000000000009
		;
createNode transform -n "wrist_ik_Con_ref" -p "wrist_ik_Con";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 -1.4791141972894017e-031 0 ;
createNode transform -n "wrist_ik_piv_space" -p "wrist_ik_Con";
	setAttr ".t" -type "double3" -1.9706458687096525e-015 0 0 ;
	setAttr ".r" -type "double3" 0 1.1131941385122312e-014 0 ;
createNode transform -n "wrist_ik_piv_Con" -p "wrist_ik_piv_space";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".t" -type "double3" 1.6145726800579152e-015 0 0 ;
	setAttr ".r" -type "double3" 0 1.1131941385122312e-014 0 ;
createNode nurbsCurve -n "wrist_ik_piv_ConShape" -p "wrist_ik_piv_Con";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 21;
	setAttr ".cc" -type "nurbsCurve" 
		1 12 0 no 3
		13 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		0 0.95524734585755933 -1.4334707307777201e-031
		0 0 0.95524734585755966
		0 -0.95524734585755933 -1.4334707307777201e-031
		0 0 -0.95524734585755966
		0 0.95524734585755933 -1.4334707307777201e-031
		-0.95524734585755844 0 -1.4334707307777201e-031
		0 -0.95524734585755933 -1.4334707307777201e-031
		0.95524734585755844 0 -1.4334707307777201e-031
		0 0 0.95524734585755844
		-0.95524734585755844 0 -1.4334707307777201e-031
		0 0 -0.95524734585755844
		0.95524734585755844 0 -1.4334707307777201e-031
		0 0.95524734585755933 -1.4334707307777201e-031
		;
createNode transform -n "wrist_orbit_aim_space" -p "wrist_ik_Con";
	setAttr ".t" -type "double3" -2.075929674272281e-007 0 5.1898247477311088e-008 ;
	setAttr ".r" -type "double3" 0 -75.963759505623969 0 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
createNode transform -n "wrist_orbit_aim" -p "wrist_orbit_aim_space";
	setAttr ".t" -type "double3" 2 4.4408920985006148e-016 3.8042181236902444e-015 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
createNode transform -n "wrist_orbit_aim_vector" -p "wrist_orbit_aim";
	setAttr ".t" -type "double3" 4.4539742461923855e-017 2 7.8886090522101303e-031 ;
	setAttr ".r" -type "double3" 0 0 7.0622500768802582e-031 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 1 ;
createNode transform -n "shldr_ik_space" -p "ik_Con_space";
	setAttr ".t" -type "double3" 2.0223748683929443 0 -5.5511151231257827e-017 ;
	setAttr ".r" -type "double3" 0 98.530765609948091 0 ;
	setAttr ".s" -type "double3" 0.99999999999999956 1 0.99999999999999956 ;
createNode transform -n "shldr_ik_Con" -p "shldr_ik_space";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".r" -type "double3" -3.4654449142822017e-015 3.1805546814635168e-015 -3.0179478298548136e-014 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
createNode nurbsCurve -n "shldr_ik_ConShape" -p "shldr_ik_Con";
	setAttr -k off ".v";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".cc" -type "nurbsCurve" 
		1 5 0 no 3
		6 0 1 2 3 4 5
		6
		0 0 0
		0 1.0000000000000002 0
		0 1.5 0.5
		0 2 0
		0 1.5 -0.5
		0 1.0000000000000002 0
		;
createNode transform -n "shldr_ik_Con_ref" -p "shldr_ik_Con";
createNode orientConstraint -n "shldr_ik_Con_ref_orientConstraint1" -p "shldr_ik_Con_ref";
	addAttr -ci true -k true -sn "w0" -ln "uparm_basis_ik_jnt_refW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" -1.2273598689145518e-006 -104.03624346792643 0 ;
	setAttr ".rsrr" -type "double3" 0 -104.03624346792644 0 ;
	setAttr -k on ".w0";
createNode transform -n "arm_pole_ik_space" -p "ik_Con_placement";
	setAttr ".t" -type "double3" 6.8681629706703262 0 5.3402563054888041 ;
	setAttr ".r" -type "double3" 0 98.530765609948091 0 ;
	setAttr ".s" -type "double3" 0.99999999999999956 0.99999999999999956 0.99999999999999911 ;
createNode transform -n "arm_pole_ik_Con" -p "arm_pole_ik_space";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 0 8.8817841970012523e-016 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000004 1.0000000000000004 ;
createNode nurbsCurve -n "arm_pole_ik_ConShape" -p "arm_pole_ik_Con";
	setAttr -k off ".v";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-0.5 -0.5 0.5
		0.5 -0.5 0.5
		0.5 -0.5 -0.5
		-0.5 -0.5 -0.5
		-0.5 -0.5 0.5
		-0.5 0.5 0.5
		-0.5 0.5 -0.5
		-0.5 -0.5 -0.5
		0.5 -0.5 -0.5
		0.5 0.5 -0.5
		0.5 0.5 0.5
		0.5 -0.5 0.5
		-0.5 -0.5 0.5
		-0.5 0.5 0.5
		0.5 0.5 0.5
		0.5 0.5 -0.5
		-0.5 0.5 -0.5
		;
createNode transform -n "arm_pole_ik_Con_ref" -p "arm_pole_ik_Con";
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999933 0.99999999999999933 ;
createNode transform -n "fk_Con_placement" -p "motion_control";
	setAttr ".t" -type "double3" 0.3 0 1 ;
	setAttr ".r" -type "double3" 0 261.46923439005189 0 ;
createNode transform -n "fk_Con_space" -p "fk_Con_placement";
	setAttr ".t" -type "double3" 7.7715611723760978e-016 0 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1.0000000000000002 ;
createNode transform -n "clavicle_fk_space" -p "fk_Con_space";
	setAttr ".t" -type "double3" 0 0 5.5511151231257827e-017 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode transform -n "clavicle_fk_Con" -p "clavicle_fk_space";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".s" -type "double3" 1.0000000000000029 1.0000000000000022 1.0000000000000018 ;
createNode nurbsCurve -n "clavicle_fk_ConShape" -p "clavicle_fk_Con";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 36 0 no 3
		37 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36
		37
		0 0.55393126112809177 0
		0.27696563056404599 0.48025840339805526 0
		0.48001473013194274 0.27696563056404588 0
		0.55393126112809177 0 0
		0.48003045547308398 -0.27696563056404588 0
		0.27696563056404588 -0.48025840339805526 0
		0 -0.55393126112809177 0
		-0.27696563056404588 -0.48025840339805526 0
		-0.48025840339805526 -0.27696563056404588 0
		-0.55393126112809177 0 0
		-0.48025840339805526 0.27696563056404588 0
		-0.27696563056404588 0.48025840339805526 0
		0 0.55393126112809177 0
		0 0.48025840339805526 0.27696563056404588
		0 0.27696563056404588 0.48019762222290113
		0 0 0.55393126112809177
		0 -0.27696563056404588 0.48025840339805526
		0 -0.48025840339805526 0.27696563056404588
		0 -0.55393126112809177 0
		0 -0.48025840339805526 -0.27696563056404588
		0 -0.27696563056404588 -0.48025840339805526
		0 0 -0.55393126112809177
		0.27696563056404588 0 -0.48025840339805526
		0.48025840339805526 0 -0.27696563056404588
		0.55393126112809177 0 0
		0.47837382395141032 0 0.27831035069991489
		0.27696563056404588 0 0.48025840339805526
		0 0 0.55393126112809177
		-0.27696563056404588 0 0.48025840339805526
		-0.47672158522815616 0 0.27996258942316909
		-0.55393126112809177 0 0
		-0.48025840339805526 0 -0.27696563056404588
		-0.27696563056404588 0 -0.48025840339805526
		0 0 -0.55393126112809177
		0 0.27696563056404588 -0.48025840339805526
		0 0.48025840339805526 -0.27696563056404588
		0 0.55393126112809177 0
		;
createNode transform -n "uparm_fk_space" -p "clavicle_fk_Con";
	setAttr ".t" -type "double3" 2.0223748416156684 0 -3.3306690738754696e-016 ;
	setAttr ".r" -type "double3" 0 -5.5054778579783541 0 ;
createNode transform -n "uparm_fk_Con" -p "uparm_fk_space";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".s" -type "double3" 1.0000000000000029 1.0000000000000022 1.0000000000000018 ;
createNode nurbsCurve -n "uparm_fk_ConShape" -p "uparm_fk_Con";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 36 0 no 3
		37 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36
		37
		0 0.55393126112809177 0
		0.27696563056404599 0.48025840339805526 0
		0.48001473013194274 0.27696563056404588 0
		0.55393126112809177 0 0
		0.48003045547308398 -0.27696563056404588 0
		0.27696563056404588 -0.48025840339805526 0
		0 -0.55393126112809177 0
		-0.27696563056404588 -0.48025840339805526 0
		-0.48025840339805526 -0.27696563056404588 0
		-0.55393126112809177 0 0
		-0.48025840339805526 0.27696563056404588 0
		-0.27696563056404588 0.48025840339805526 0
		0 0.55393126112809177 0
		0 0.48025840339805526 0.27696563056404588
		0 0.27696563056404588 0.48019762222290113
		0 0 0.55393126112809177
		0 -0.27696563056404588 0.48025840339805526
		0 -0.48025840339805526 0.27696563056404588
		0 -0.55393126112809177 0
		0 -0.48025840339805526 -0.27696563056404588
		0 -0.27696563056404588 -0.48025840339805526
		0 0 -0.55393126112809177
		0.27696563056404588 0 -0.48025840339805526
		0.48025840339805526 0 -0.27696563056404588
		0.55393126112809177 0 0
		0.47837382395141032 0 0.27831035069991489
		0.27696563056404588 0 0.48025840339805526
		0 0 0.55393126112809177
		-0.27696563056404588 0 0.48025840339805526
		-0.47672158522815616 0 0.27996258942316909
		-0.55393126112809177 0 0
		-0.48025840339805526 0 -0.27696563056404588
		-0.27696563056404588 0 -0.48025840339805526
		0 0 -0.55393126112809177
		0 0.27696563056404588 -0.48025840339805526
		0 0.48025840339805526 -0.27696563056404588
		0 0.55393126112809177 0
		;
createNode transform -n "loarm_fk_space" -p "uparm_fk_Con";
	setAttr ".t" -type "double3" 4.1231056256176597 0 -1.3322676295501878e-015 ;
	setAttr ".r" -type "double3" 0 28.072486935852968 0 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
createNode transform -n "loarm_fk_Con" -p "loarm_fk_space";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".s" -type "double3" 1.0000000000000024 1.0000000000000022 1.0000000000000016 ;
createNode nurbsCurve -n "loarm_fk_ConShape" -p "loarm_fk_Con";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 36 0 no 3
		37 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36
		37
		0 0.55393126112809177 0
		0.27696563056404599 0.48025840339805526 0
		0.48001473013194274 0.27696563056404588 0
		0.55393126112809177 0 0
		0.48003045547308398 -0.27696563056404588 0
		0.27696563056404588 -0.48025840339805526 0
		0 -0.55393126112809177 0
		-0.27696563056404588 -0.48025840339805526 0
		-0.48025840339805526 -0.27696563056404588 0
		-0.55393126112809177 0 0
		-0.48025840339805526 0.27696563056404588 0
		-0.27696563056404588 0.48025840339805526 0
		0 0.55393126112809177 0
		0 0.48025840339805526 0.27696563056404588
		0 0.27696563056404588 0.48019762222290113
		0 0 0.55393126112809177
		0 -0.27696563056404588 0.48025840339805526
		0 -0.48025840339805526 0.27696563056404588
		0 -0.55393126112809177 0
		0 -0.48025840339805526 -0.27696563056404588
		0 -0.27696563056404588 -0.48025840339805526
		0 0 -0.55393126112809177
		0.27696563056404588 0 -0.48025840339805526
		0.48025840339805526 0 -0.27696563056404588
		0.55393126112809177 0 0
		0.47837382395141032 0 0.27831035069991489
		0.27696563056404588 0 0.48025840339805526
		0 0 0.55393126112809177
		-0.27696563056404588 0 0.48025840339805526
		-0.47672158522815616 0 0.27996258942316909
		-0.55393126112809177 0 0
		-0.48025840339805526 0 -0.27696563056404588
		-0.27696563056404588 0 -0.48025840339805526
		0 0 -0.55393126112809177
		0 0.27696563056404588 -0.48025840339805526
		0 0.48025840339805526 -0.27696563056404588
		0 0.55393126112809177 0
		;
createNode transform -n "wrist_fk_space" -p "loarm_fk_Con";
	setAttr ".t" -type "double3" 4.1231056256176624 0 0 ;
	setAttr ".s" -type "double3" 1.0000000000000004 1.0000000000000002 1.0000000000000002 ;
createNode transform -n "wrist_fk_Con" -p "wrist_fk_space";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".s" -type "double3" 1.0000000000000029 1.0000000000000022 1.000000000000002 ;
createNode nurbsCurve -n "wrist_fk_ConShape" -p "wrist_fk_Con";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 36 0 no 3
		37 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36
		37
		0 0.55393126112809177 0
		0.27696563056404599 0.48025840339805526 0
		0.48001473013194274 0.27696563056404588 0
		0.55393126112809177 0 0
		0.48003045547308398 -0.27696563056404588 0
		0.27696563056404588 -0.48025840339805526 0
		0 -0.55393126112809177 0
		-0.27696563056404588 -0.48025840339805526 0
		-0.48025840339805526 -0.27696563056404588 0
		-0.55393126112809177 0 0
		-0.48025840339805526 0.27696563056404588 0
		-0.27696563056404588 0.48025840339805526 0
		0 0.55393126112809177 0
		0 0.48025840339805526 0.27696563056404588
		0 0.27696563056404588 0.48019762222290113
		0 0 0.55393126112809177
		0 -0.27696563056404588 0.48025840339805526
		0 -0.48025840339805526 0.27696563056404588
		0 -0.55393126112809177 0
		0 -0.48025840339805526 -0.27696563056404588
		0 -0.27696563056404588 -0.48025840339805526
		0 0 -0.55393126112809177
		0.27696563056404588 0 -0.48025840339805526
		0.48025840339805526 0 -0.27696563056404588
		0.55393126112809177 0 0
		0.47837382395141032 0 0.27831035069991489
		0.27696563056404588 0 0.48025840339805526
		0 0 0.55393126112809177
		-0.27696563056404588 0 0.48025840339805526
		-0.47672158522815616 0 0.27996258942316909
		-0.55393126112809177 0 0
		-0.48025840339805526 0 -0.27696563056404588
		-0.27696563056404588 0 -0.48025840339805526
		0 0 -0.55393126112809177
		0 0.27696563056404588 -0.48025840339805526
		0 0.48025840339805526 -0.27696563056404588
		0 0.55393126112809177 0
		;
createNode transform -n "spaceWeights";
	addAttr -ci true -sn "All" -ln "All" -nn "All" -at "double";
	addAttr -ci true -sn "Body" -ln "Body" -nn "Body" -at "double";
	addAttr -ci true -sn "Hip" -ln "Hip" -nn "Hip" -at "double";
	setAttr -k on ".All";
	setAttr -k on ".Body";
	setAttr -k on ".Hip";
createNode transform -n "input2";
	addAttr -ci true -sn "body2All" -ln "body2All" -nn "Body 2 All" -dv 1 -min 0 -max 
		1 -at "double";
	addAttr -ci true -sn "hip2Body" -ln "hip2Body" -nn "Hip 2 Body" -dv 1 -min 0 -max 
		1 -at "double";
	setAttr -l on -k off ".v" no;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".body2All";
	setAttr -k on ".hip2Body";
createNode transform -n "output2";
	addAttr -ci true -sn "all" -ln "all" -nn "All" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "body" -ln "body" -nn "Body" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "hip" -ln "hip" -nn "Hip" -min 0 -max 1 -at "double";
	setAttr -l on -k off ".v" no;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".all";
	setAttr -k on ".body";
	setAttr -k on ".hip";
createNode lightLinker -s -n "lightLinker1";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode displayLayerManager -n "layerManager";
createNode displayLayer -n "defaultLayer";
createNode renderLayerManager -n "renderLayerManager";
createNode renderLayer -n "defaultRenderLayer";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"top\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n"
		+ "                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n"
		+ "                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n"
		+ "                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n"
		+ "            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n"
		+ "            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"side\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n"
		+ "                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n"
		+ "                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n"
		+ "                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n"
		+ "            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n"
		+ "            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"front\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n"
		+ "                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n"
		+ "                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n"
		+ "                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n"
		+ "            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n"
		+ "            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n"
		+ "        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n"
		+ "                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n"
		+ "                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n"
		+ "                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n"
		+ "            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n"
		+ "            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n"
		+ "            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            outlinerEditor -e \n                -showShapes 0\n                -showReferenceNodes 1\n                -showReferenceMembers 1\n                -showAttributes 0\n                -showConnected 0\n                -showAnimCurvesOnly 0\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n"
		+ "                -autoExpand 0\n                -showDagOnly 1\n                -showAssets 1\n                -showContainedOnly 1\n                -showPublishedAsConnected 0\n                -showContainerContents 1\n                -ignoreDagHierarchy 0\n                -expandConnections 0\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 0\n                -highlightActive 1\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"defaultSetFilter\" \n                -showSetMembers 1\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n"
		+ "                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n"
		+ "            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n"
		+ "            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"graphEditor\" -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n"
		+ "                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n"
		+ "                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1.25\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n"
		+ "                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n"
		+ "                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n"
		+ "                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1.25\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n"
		+ "                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dopeSheetPanel\" -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n"
		+ "                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n"
		+ "                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n"
		+ "                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n"
		+ "                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"clipEditorPanel\" -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n"
		+ "                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"sequenceEditorPanel\" -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n"
		+ "                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n"
		+ "                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperShadePanel\" -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"visorPanel\" -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n"
		+ "            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -ignoreAssets 1\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -keyReleaseCommand \"nodeEdKeyReleaseCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -island 0\n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -syncedSelection 1\n                -extendToShapes 1\n                $editorName;\n\t\t\tif (`objExists nodeEditorPanel1Info`) nodeEditor -e -restoreInfo nodeEditorPanel1Info $editorName;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -ignoreAssets 1\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -keyReleaseCommand \"nodeEdKeyReleaseCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -island 0\n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n"
		+ "                -syncedSelection 1\n                -extendToShapes 1\n                $editorName;\n\t\t\tif (`objExists nodeEditorPanel1Info`) nodeEditor -e -restoreInfo nodeEditorPanel1Info $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"createNodePanel\" -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Texture Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"polyTexturePlacementPanel\" -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"renderWindowPanel\" -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"blendShapePanel\" (localizedPanelLabel(\"Blend Shape\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\tblendShapePanel -unParent -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels ;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tblendShapePanel -edit -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynRelEdPanel\" -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"relationshipPanel\" -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"referenceEditorPanel\" -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"componentEditorPanel\" -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynPaintScriptedPanelType\" -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"scriptEditorPanel\" -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\tif ($useSceneConfig) {\n\t\tscriptedPanel -e -to $panelName;\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph InputOutput3\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph InputOutput3\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n"
		+ "                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -currentNode \"R:Arm:module:clavicle_child_plug\" \n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"largeIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph InputOutput3\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n"
		+ "                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -currentNode \"R:Arm:module:clavicle_child_plug\" \n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"largeIcons\" \n                -showCachedConnections 0\n"
		+ "                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\tif ($useSceneConfig) {\n\t\tscriptedPanel -e -to $panelName;\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"createNodePanel\" -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph InputOutput4\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph InputOutput4\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n"
		+ "            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n"
		+ "                -showCachedConnections 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph InputOutput4\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n"
		+ "                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph InputOutput5\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph InputOutput5\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n"
		+ "                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph InputOutput5\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n"
		+ "            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n"
		+ "                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph InputOutput6\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph InputOutput6\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showUnderworld 0\n                -showInvisible 0\n"
		+ "                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph InputOutput6\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n"
		+ "                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph InputOutput7\")) `;\n\tif (\"\" == $panelName) {\n"
		+ "\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph InputOutput7\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n"
		+ "                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph InputOutput7\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showUnderworld 0\n                -showInvisible 0\n"
		+ "                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph InputOutput1\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph InputOutput1\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n"
		+ "                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1.3275\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 5\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"largeIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\t}\n"
		+ "\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph InputOutput1\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1.3275\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 5\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n"
		+ "                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"largeIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\tif ($useSceneConfig) {\n\t\tscriptedPanel -e -to $panelName;\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-defaultImage \"\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"vertical2\\\" -ps 1 33 100 -ps 2 67 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Outliner\")) \n\t\t\t\t\t\"outlinerPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\\\"Outliner\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\noutlinerEditor -e \\n    -showShapes 0\\n    -showReferenceNodes 1\\n    -showReferenceMembers 1\\n    -showAttributes 0\\n    -showConnected 0\\n    -showAnimCurvesOnly 0\\n    -showMuteInfo 0\\n    -organizeByLayer 1\\n    -showAnimLayerWeight 1\\n    -autoExpandLayers 1\\n    -autoExpand 0\\n    -showDagOnly 1\\n    -showAssets 1\\n    -showContainedOnly 1\\n    -showPublishedAsConnected 0\\n    -showContainerContents 1\\n    -ignoreDagHierarchy 0\\n    -expandConnections 0\\n    -showUpstreamCurves 1\\n    -showUnitlessCurves 1\\n    -showCompounds 1\\n    -showLeafs 1\\n    -showNumericAttrsOnly 0\\n    -highlightActive 1\\n    -autoSelectNewObjects 0\\n    -doNotSelectNewObjects 0\\n    -dropIsParent 1\\n    -transmitFilters 0\\n    -setFilter \\\"defaultSetFilter\\\" \\n    -showSetMembers 1\\n    -allowMultiSelection 1\\n    -alwaysToggleSelect 0\\n    -directSelect 0\\n    -displayMode \\\"DAG\\\" \\n    -expandObjects 0\\n    -setsIgnoreFilters 1\\n    -containersIgnoreFilters 0\\n    -editAttrName 0\\n    -showAttrValues 0\\n    -highlightSecondary 0\\n    -showUVAttrsOnly 0\\n    -showTextureNodesOnly 0\\n    -attrAlphaOrder \\\"default\\\" \\n    -animLayerFilterOptions \\\"allAffecting\\\" \\n    -sortOrder \\\"none\\\" \\n    -longNames 0\\n    -niceNames 1\\n    -showNamespace 1\\n    -showPinIcons 0\\n    -mapMotionTrails 0\\n    $editorName\"\n"
		+ "\t\t\t\t\t\"outlinerPanel -edit -l (localizedPanelLabel(\\\"Outliner\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\noutlinerEditor -e \\n    -showShapes 0\\n    -showReferenceNodes 1\\n    -showReferenceMembers 1\\n    -showAttributes 0\\n    -showConnected 0\\n    -showAnimCurvesOnly 0\\n    -showMuteInfo 0\\n    -organizeByLayer 1\\n    -showAnimLayerWeight 1\\n    -autoExpandLayers 1\\n    -autoExpand 0\\n    -showDagOnly 1\\n    -showAssets 1\\n    -showContainedOnly 1\\n    -showPublishedAsConnected 0\\n    -showContainerContents 1\\n    -ignoreDagHierarchy 0\\n    -expandConnections 0\\n    -showUpstreamCurves 1\\n    -showUnitlessCurves 1\\n    -showCompounds 1\\n    -showLeafs 1\\n    -showNumericAttrsOnly 0\\n    -highlightActive 1\\n    -autoSelectNewObjects 0\\n    -doNotSelectNewObjects 0\\n    -dropIsParent 1\\n    -transmitFilters 0\\n    -setFilter \\\"defaultSetFilter\\\" \\n    -showSetMembers 1\\n    -allowMultiSelection 1\\n    -alwaysToggleSelect 0\\n    -directSelect 0\\n    -displayMode \\\"DAG\\\" \\n    -expandObjects 0\\n    -setsIgnoreFilters 1\\n    -containersIgnoreFilters 0\\n    -editAttrName 0\\n    -showAttrValues 0\\n    -highlightSecondary 0\\n    -showUVAttrsOnly 0\\n    -showTextureNodesOnly 0\\n    -attrAlphaOrder \\\"default\\\" \\n    -animLayerFilterOptions \\\"allAffecting\\\" \\n    -sortOrder \\\"none\\\" \\n    -longNames 0\\n    -niceNames 1\\n    -showNamespace 1\\n    -showPinIcons 0\\n    -mapMotionTrails 0\\n    $editorName\"\n"
		+ "\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"wireframe\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"wireframe\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        setFocus `paneLayout -q -p1 $gMainPane`;\n        sceneUIReplacement -deleteRemaining;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	setAttr ".b" -type "string" "playbackOptions -min 0 -max 100 -ast 0 -aet 100 ";
	setAttr ".st" 6;
createNode ikRPsolver -n "ikRPsolver";
createNode container -n "spaceRemapOp_arm";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".isc" yes;
	setAttr -s 5 ".boc";
	setAttr ".ctor" -type "string" "hyunseungkim";
	setAttr ".cdat" -type "string" "2015/09/20 13:30:21";
	setAttr ".aal" -type "attributeAlias" {"Out_all","borderConnections[0]","Out_body"
		,"borderConnections[1]","Out_hip","borderConnections[2]","In_body2All","borderConnections[3]"
		,"In_hip2Body","borderConnections[4]"} ;
createNode remapValue -n "body2all_remap";
	setAttr ".omn" 1;
	setAttr ".omx" 0;
	setAttr -s 2 ".vl[0:1]"  0 0 1 1 1 1;
	setAttr -s 2 ".cl";
	setAttr ".cl[0].cli" 1;
	setAttr ".cl[1].clp" 1;
	setAttr ".cl[1].clc" -type "float3" 1 1 1 ;
	setAttr ".cl[1].cli" 1;
createNode multiplyDivide -n "apply_hip2body_weight";
createNode plusMinusAverage -n "remain_hip_weight";
	setAttr ".op" 2;
	setAttr -s 2 ".i3[0:1]" -type "float3"  0 0 0 0 0 0;
	setAttr -s 2 ".i3";
createNode hyperLayout -n "hyperLayout3";
	setAttr ".ihi" 0;
	setAttr -s 6 ".hyp";
	setAttr ".hyp[0].x" 68;
	setAttr ".hyp[0].y" 129;
	setAttr ".hyp[0].isf" yes;
	setAttr ".hyp[1].x" 447;
	setAttr ".hyp[1].y" 54;
	setAttr ".hyp[1].isf" yes;
	setAttr ".hyp[2].x" 259;
	setAttr ".hyp[2].y" 92;
	setAttr ".hyp[2].isf" yes;
	setAttr ".hyp[3].x" 71;
	setAttr ".hyp[3].y" 54;
	setAttr ".hyp[3].isf" yes;
	setAttr ".hyp[4].x" 259;
	setAttr ".hyp[4].y" 16;
	setAttr ".hyp[4].isf" yes;
	setAttr ".hyp[5].x" 635;
	setAttr ".hyp[5].y" 54;
	setAttr ".hyp[5].isf" yes;
	setAttr ".anf" yes;
createNode condition -n "ik_con_display_condition";
	setAttr ".st" 1;
	setAttr ".ct" -type "float3" 1 0 0 ;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode condition -n "fk_con_display_condition";
	setAttr ".ct" -type "float3" 1 0 0 ;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode hyperGraphInfo -n "nodeEditorPanel1Info";
createNode hyperView -n "hyperView1";
	setAttr ".dag" no;
createNode hyperLayout -n "hyperLayout4";
	setAttr ".ihi" 0;
	setAttr -s 22 ".hyp";
	setAttr ".hyp[0].nvs" 1920;
	setAttr ".hyp[1].nvs" 1920;
	setAttr ".hyp[2].nvs" 1920;
	setAttr ".hyp[3].nvs" 1920;
	setAttr ".hyp[4].nvs" 1920;
	setAttr ".hyp[5].nvs" 1920;
	setAttr ".hyp[6].nvs" 1920;
	setAttr ".hyp[7].nvs" 1920;
	setAttr ".hyp[8].nvs" 1920;
	setAttr ".hyp[9].nvs" 1920;
	setAttr ".hyp[10].nvs" 1920;
	setAttr ".hyp[11].nvs" 1920;
	setAttr ".hyp[12].nvs" 1920;
	setAttr ".hyp[13].nvs" 1920;
	setAttr ".hyp[14].nvs" 1920;
	setAttr ".hyp[15].nvs" 1920;
	setAttr ".hyp[16].nvs" 1920;
	setAttr ".hyp[17].nvs" 1920;
	setAttr ".hyp[18].nvs" 1920;
	setAttr ".hyp[19].nvs" 1920;
	setAttr ".hyp[20].nvs" 1920;
	setAttr ".hyp[21].nvs" 1920;
	setAttr ".anf" yes;
select -ne :time1;
	setAttr ".o" 0;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultShaderList1;
	setAttr -s 2 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 5 ".u";
select -ne :defaultRenderingList1;
select -ne :renderGlobalsList1;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 18 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surfaces" "Particles" "Fluids" "Image Planes" "UI:" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 18 0 1 1 1 1 1
		 1 0 0 0 0 0 0 0 0 0 0 0 ;
select -ne :defaultHardwareRenderGlobals;
	setAttr ".fn" -type "string" "im";
	setAttr ".res" -type "string" "ntsc_4d 646 485 1.333";
select -ne :ikSystem;
connectAttr "clavicle_fk_jnt.s" "uparm_fk_jnt.is";
connectAttr "uparm_fk_jnt.s" "loarm_fk_jnt.is";
connectAttr "loarm_fk_jnt.s" "wrist_fk_jnt.is";
connectAttr "uparm_basis_ik_jnt.s" "loarm_basis_ik_jnt.is";
connectAttr "loarm_basis_ik_jnt.s" "wrist_basis_ik_jnt.is";
connectAttr "wrist_basis_ik_jnt.tx" "effector1.tx";
connectAttr "wrist_basis_ik_jnt.ty" "effector1.ty";
connectAttr "wrist_basis_ik_jnt.tz" "effector1.tz";
connectAttr "uparm_basis_ik_jnt.msg" "arm_basis_ik_handle.hsj";
connectAttr "effector1.hp" "arm_basis_ik_handle.hee";
connectAttr "ikRPsolver.msg" "arm_basis_ik_handle.hsv";
connectAttr "arm_basis_ikHandle_poleVectorConstraint1.ctx" "arm_basis_ik_handle.pvx"
		;
connectAttr "arm_basis_ikHandle_poleVectorConstraint1.cty" "arm_basis_ik_handle.pvy"
		;
connectAttr "arm_basis_ikHandle_poleVectorConstraint1.ctz" "arm_basis_ik_handle.pvz"
		;
connectAttr "arm_basis_ik_handle.pim" "arm_basis_ikHandle_poleVectorConstraint1.cpim"
		;
connectAttr "uparm_basis_ik_jnt.pm" "arm_basis_ikHandle_poleVectorConstraint1.ps"
		;
connectAttr "uparm_basis_ik_jnt.t" "arm_basis_ikHandle_poleVectorConstraint1.crp"
		;
connectAttr "arm_pole_ik_Con_ref.t" "arm_basis_ikHandle_poleVectorConstraint1.tg[0].tt"
		;
connectAttr "arm_pole_ik_Con_ref.rp" "arm_basis_ikHandle_poleVectorConstraint1.tg[0].trp"
		;
connectAttr "arm_pole_ik_Con_ref.rpt" "arm_basis_ikHandle_poleVectorConstraint1.tg[0].trt"
		;
connectAttr "arm_pole_ik_Con_ref.pm" "arm_basis_ikHandle_poleVectorConstraint1.tg[0].tpm"
		;
connectAttr "arm_basis_ikHandle_poleVectorConstraint1.w0" "arm_basis_ikHandle_poleVectorConstraint1.tg[0].tw"
		;
connectAttr "clavicle_ik_jnt.s" "uparm_ik_jnt.is";
connectAttr "uparm_ik_jnt.s" "loarm_ik_jnt.is";
connectAttr "loarm_ik_jnt.s" "wrist_ik_jnt.is";
connectAttr "wrist_ik_jnt.tx" "effector4.tx";
connectAttr "wrist_ik_jnt.ty" "effector4.ty";
connectAttr "wrist_ik_jnt.tz" "effector4.tz";
connectAttr "uparm_ik_jnt.tx" "effector3.tx";
connectAttr "uparm_ik_jnt.ty" "effector3.ty";
connectAttr "uparm_ik_jnt.tz" "effector3.tz";
connectAttr "uparm_ik_jnt.msg" "arm_ik_handle.hsj";
connectAttr "effector4.hp" "arm_ik_handle.hee";
connectAttr "ikRPsolver.msg" "arm_ik_handle.hsv";
connectAttr "arm_ik_handle_poleVectorConstraint1.ctx" "arm_ik_handle.pvx";
connectAttr "arm_ik_handle_poleVectorConstraint1.cty" "arm_ik_handle.pvy";
connectAttr "arm_ik_handle_poleVectorConstraint1.ctz" "arm_ik_handle.pvz";
connectAttr "arm_ik_handle.pim" "arm_ik_handle_poleVectorConstraint1.cpim";
connectAttr "uparm_ik_jnt.pm" "arm_ik_handle_poleVectorConstraint1.ps";
connectAttr "uparm_ik_jnt.t" "arm_ik_handle_poleVectorConstraint1.crp";
connectAttr "arm_pole_ik_Con_ref.t" "arm_ik_handle_poleVectorConstraint1.tg[0].tt"
		;
connectAttr "arm_pole_ik_Con_ref.rp" "arm_ik_handle_poleVectorConstraint1.tg[0].trp"
		;
connectAttr "arm_pole_ik_Con_ref.rpt" "arm_ik_handle_poleVectorConstraint1.tg[0].trt"
		;
connectAttr "arm_pole_ik_Con_ref.pm" "arm_ik_handle_poleVectorConstraint1.tg[0].tpm"
		;
connectAttr "arm_ik_handle_poleVectorConstraint1.w0" "arm_ik_handle_poleVectorConstraint1.tg[0].tw"
		;
connectAttr "clavicle_ik_jnt.msg" "shldr_ik_handle.hsj";
connectAttr "effector3.hp" "shldr_ik_handle.hee";
connectAttr "ikRPsolver.msg" "shldr_ik_handle.hsv";
connectAttr "shldr_ik_handle_poleVectorConstraint1.ctx" "shldr_ik_handle.pvx";
connectAttr "shldr_ik_handle_poleVectorConstraint1.cty" "shldr_ik_handle.pvy";
connectAttr "shldr_ik_handle_poleVectorConstraint1.ctz" "shldr_ik_handle.pvz";
connectAttr "shldr_ik_handle.pim" "shldr_ik_handle_poleVectorConstraint1.cpim";
connectAttr "clavicle_ik_jnt.pm" "shldr_ik_handle_poleVectorConstraint1.ps";
connectAttr "clavicle_ik_jnt.t" "shldr_ik_handle_poleVectorConstraint1.crp";
connectAttr "arm_pole_ik_Con_ref.t" "shldr_ik_handle_poleVectorConstraint1.tg[0].tt"
		;
connectAttr "arm_pole_ik_Con_ref.rp" "shldr_ik_handle_poleVectorConstraint1.tg[0].trp"
		;
connectAttr "arm_pole_ik_Con_ref.rpt" "shldr_ik_handle_poleVectorConstraint1.tg[0].trt"
		;
connectAttr "arm_pole_ik_Con_ref.pm" "shldr_ik_handle_poleVectorConstraint1.tg[0].tpm"
		;
connectAttr "shldr_ik_handle_poleVectorConstraint1.w0" "shldr_ik_handle_poleVectorConstraint1.tg[0].tw"
		;
connectAttr "clavicle_auto_ik_jnt.s" "uparm_auto_ik_jnt.is";
connectAttr "uparm_auto_ik_jnt.tx" "effector2.tx";
connectAttr "uparm_auto_ik_jnt.ty" "effector2.ty";
connectAttr "uparm_auto_ik_jnt.tz" "effector2.tz";
connectAttr "clavicle_auto_ik_jnt.msg" "shldr_auto_ik_handle.hsj";
connectAttr "effector2.hp" "shldr_auto_ik_handle.hee";
connectAttr "ikRPsolver.msg" "shldr_auto_ik_handle.hsv";
connectAttr "shldr_auto_ik_handle_poleVectorConstraint1.ctx" "shldr_auto_ik_handle.pvx"
		;
connectAttr "shldr_auto_ik_handle_poleVectorConstraint1.cty" "shldr_auto_ik_handle.pvy"
		;
connectAttr "shldr_auto_ik_handle_poleVectorConstraint1.ctz" "shldr_auto_ik_handle.pvz"
		;
connectAttr "shldr_auto_ik_handle.pim" "shldr_auto_ik_handle_poleVectorConstraint1.cpim"
		;
connectAttr "clavicle_auto_ik_jnt.pm" "shldr_auto_ik_handle_poleVectorConstraint1.ps"
		;
connectAttr "clavicle_auto_ik_jnt.t" "shldr_auto_ik_handle_poleVectorConstraint1.crp"
		;
connectAttr "arm_pole_ik_Con_ref.t" "shldr_auto_ik_handle_poleVectorConstraint1.tg[0].tt"
		;
connectAttr "arm_pole_ik_Con_ref.rp" "shldr_auto_ik_handle_poleVectorConstraint1.tg[0].trp"
		;
connectAttr "arm_pole_ik_Con_ref.rpt" "shldr_auto_ik_handle_poleVectorConstraint1.tg[0].trt"
		;
connectAttr "arm_pole_ik_Con_ref.pm" "shldr_auto_ik_handle_poleVectorConstraint1.tg[0].tpm"
		;
connectAttr "shldr_auto_ik_handle_poleVectorConstraint1.w0" "shldr_auto_ik_handle_poleVectorConstraint1.tg[0].tw"
		;
connectAttr "clavicle_blend_jnt.s" "uparm_blend_jnt.is";
connectAttr "uparm_blend_jnt.s" "loarm_blend_jnt.is";
connectAttr "loarm_blend_jnt.s" "wrist_blend_jnt.is";
connectAttr "ik_con_display_condition.ocr" "ik_Con_placement.v";
connectAttr "wrist_orbit_aim.tx" "wrist_orbit_aim_vector.ty";
connectAttr "shldr_ik_Con_ref_orientConstraint1.crx" "shldr_ik_Con_ref.rx";
connectAttr "shldr_ik_Con_ref_orientConstraint1.cry" "shldr_ik_Con_ref.ry";
connectAttr "shldr_ik_Con_ref_orientConstraint1.crz" "shldr_ik_Con_ref.rz";
connectAttr "shldr_ik_Con_ref.ro" "shldr_ik_Con_ref_orientConstraint1.cro";
connectAttr "shldr_ik_Con_ref.pim" "shldr_ik_Con_ref_orientConstraint1.cpim";
connectAttr "uparm_basis_ik_jnt_ref.r" "shldr_ik_Con_ref_orientConstraint1.tg[0].tr"
		;
connectAttr "uparm_basis_ik_jnt_ref.ro" "shldr_ik_Con_ref_orientConstraint1.tg[0].tro"
		;
connectAttr "uparm_basis_ik_jnt_ref.pm" "shldr_ik_Con_ref_orientConstraint1.tg[0].tpm"
		;
connectAttr "shldr_ik_Con_ref_orientConstraint1.w0" "shldr_ik_Con_ref_orientConstraint1.tg[0].tw"
		;
connectAttr "fk_con_display_condition.ocr" "fk_Con_placement.v";
connectAttr "input2.body2All" "spaceWeights.All";
connectAttr "apply_hip2body_weight.ox" "spaceWeights.Body";
connectAttr "remain_hip_weight.o3x" "spaceWeights.Hip";
connectAttr "wrist_ik_Con.spaceUpbody2All" "input2.body2All";
connectAttr "wrist_ik_Con.spaceChest2Upbody" "input2.hip2Body";
connectAttr "spaceWeights.All" "output2.all";
connectAttr "spaceWeights.Body" "output2.body";
connectAttr "spaceWeights.Hip" "output2.hip";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "output2.all" "spaceRemapOp_arm.boc[0]";
connectAttr "output2.body" "spaceRemapOp_arm.boc[1]";
connectAttr "output2.hip" "spaceRemapOp_arm.boc[2]";
connectAttr "input2.body2All" "spaceRemapOp_arm.boc[3]";
connectAttr "input2.hip2Body" "spaceRemapOp_arm.boc[4]";
connectAttr "hyperLayout3.msg" "spaceRemapOp_arm.hl";
connectAttr "input2.body2All" "body2all_remap.i";
connectAttr "body2all_remap.ov" "apply_hip2body_weight.i1x";
connectAttr "input2.hip2Body" "apply_hip2body_weight.i2x";
connectAttr "body2all_remap.ov" "remain_hip_weight.i3[0].i3x";
connectAttr "apply_hip2body_weight.ox" "remain_hip_weight.i3[1].i3x";
connectAttr "input2.msg" "hyperLayout3.hyp[0].dn";
connectAttr "spaceWeights.msg" "hyperLayout3.hyp[1].dn";
connectAttr "apply_hip2body_weight.msg" "hyperLayout3.hyp[2].dn";
connectAttr "body2all_remap.msg" "hyperLayout3.hyp[3].dn";
connectAttr "remain_hip_weight.msg" "hyperLayout3.hyp[4].dn";
connectAttr "output2.msg" "hyperLayout3.hyp[5].dn";
connectAttr "arm_fk2ik_Con.controlDisplay" "ik_con_display_condition.ft";
connectAttr "arm_fk2ik_Con.controlDisplay" "fk_con_display_condition.ft";
connectAttr "hyperView1.msg" "nodeEditorPanel1Info.b[0]";
connectAttr "hyperLayout4.msg" "hyperView1.hl";
connectAttr "wrist_orbit_aim_space.msg" "hyperLayout4.hyp[15].dn";
connectAttr "body2all_remap.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "apply_hip2body_weight.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "remain_hip_weight.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "ik_con_display_condition.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "fk_con_display_condition.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "ikRPsolver.msg" ":ikSystem.sol" -na;
// End of arm_template.ma
