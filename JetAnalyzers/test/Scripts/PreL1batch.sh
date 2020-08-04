#!/bin/bash
#set up environment and enter the workspace
export SCRAM_ARCH=slc7_amd64_gcc820
cd  /afs/cern.ch/work/b/bchitrod/private/corr_jec/CMSSW_11_1_0_pre6/src/ #modify this to your own directory!
eval $(scramv1 runtime -sh)
cd JetMETAnalysis/JetAnalyzers/test/

#----- Please modify these to your own paths ---------------
inpath="/eos/cms/store/group/phys_jetmet/bchitrod/data/11X_QCD_PU200_JRA/"
inpath2="/eos/cms/store/group/phys_jetmet/bchitrod/data/11X_QCD_NoPU_JRA/"
midpath="/eos/cms/store/group/phys_jetmet/bchitrod/data/tmp/"
outpath="/eos/cms/store/group/phys_jetmet/bchitrod/data/JEC1/PreL1/"
#-----------------------------------------------------------

num=$1
label=`printf $num`
prefix="JRA_"
string="PU_"
num2=1

outstring1="output_ak4caloHLT_"
outstring2="output_ak4pfHLT_"
outstring3="output_ak8caloHLT_"
outstring4="output_ak8pfHLT_"

# Start loop on each input file
while read file
do
	infile="$prefix$label.root"
    midfile="$prefix$string$label.root"

    echo $infile
    echo $midfile
    echo $file
	printf "Copy file from eos to tmp..."
	cp $inpath$infile $midpath
    mv  $midpath$infile   $midpath$midfile 
    cp $inpath2$file  $midpath

    label2=`printf $num2`

    # Manufacture the histograms for the subsequent parametrization
    jet_synchtest_x -basepath $midpath -samplePU $midfile -sampleNoPU $file -algo1 ak4caloHLT -algo2 ak4caloHLT  -order1 $label -order2 $label2    
    jet_synchtest_x -basepath $midpath -samplePU $midfile -sampleNoPU $file -algo1 ak4pfHLT   -algo2 ak4pfHLT    -order1 $label -order2 $label2 
    jet_synchtest_x -basepath $midpath -samplePU $midfile -sampleNoPU $file -algo1 ak8caloHLT -algo2 ak8caloHLT  -order1 $label -order2 $label2   
    jet_synchtest_x -basepath $midpath -samplePU $midfile -sampleNoPU $file -algo1 ak8pfHLT   -algo2 ak8pfHLT    -order1 $label -order2 $label2 

    outfile1=$outstring1$label"_"$label2".root"
    outfile2=$outstring2$label"_"$label2".root"
    outfile3=$outstring3$label"_"$label2".root"
    outfile4=$outstring4$label"_"$label2".root"

	printf "Copy file from tmp back to eos..."
	cp ./$outfile1 $outpath/
	cp ./$outfile2 $outpath/
	cp ./$outfile3 $outpath/
	cp ./$outfile4 $outpath/

    rm -rf $midpath/$midfile
	rm -rf $midpath/$file
	rm -rf ./$outfile1
	rm -rf ./$outfile2
	rm -rf ./$outfile3
	rm -rf ./$outfile4

    (( num2 += 1 ))

done < ./Scripts/list.txt
