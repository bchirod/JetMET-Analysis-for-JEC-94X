#!/bin/bash
#------- fit the pre-response profile -----
jet_response_fitter_x -input ./Oct1_L2L3/outputJRA.root -output ./Oct1_L2L3/outputJRA_f.root

#------- derive the L3 correction (will be merged by next step with L2 correction) ------
jet_l3_correction_x -input ./Oct1_L2L3/outputJRA_f.root -era EcalMultifitHCALMethod3 -algs ak4puppiHLT -output ./Oct1_L2L3/l3.root

#------- derive the L2 correction merged with L3 correction -------------
#jet_l2_correction_x -input ./Oct1_L2L3/outputJRA_f.root -l3input ./Oct1_L2L3/l3.root -output ./Oct1_L2L3/l2.root -era EcalMultifitHCALMethod3 -algs ak4puppiHLT ak8puppiHLT

#------ delete the redundant L3 correction files ---------
#rm EcalMultifitHCALMethod3_L3Absolute_AK4puppiHLT.txt
#rm EcalMultifitHCALMethod3_L3Absolute_AK8puppiHLT.txt

#------ change the name of L2 correction (merged with L3) files and put them together with the L1 correction files
#mv EcalMultifitHCALMethod3_L2Relative_AK4PFHLTl1.txt JECTag_EcalMultifit_HCALMethod3/
#mv EcalMultifitHCALMethod3_L2Relative_AK4CaloHLTl1.txt JECTag_EcalMultifit_HCALMethod3/
#mv EcalMultifitHCALMethod3_L2Relative_AK8PFHLTl1.txt JECTag_EcalMultifit_HCALMethod3/
#mv EcalMultifitHCALMethod3_L2Relative_AK8CaloHLTl1.txt JECTag_EcalMultifit_HCALMethod3/

#rm -rf L3*.png

# Note: You need to change the path after -input and -output in the command according to your path!
