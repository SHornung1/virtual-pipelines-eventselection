#
# python script to test the histograms
#

import sys
import ROOT

# list of histograms which should exist (only a selection for now)
required_keys = ['ggH_pt_1', 'ggH_pt_2']

file = ROOT.TFile.Open('hist_ggH.root')
keys = [k.GetName() for k in file.GetListOfKeys()]

print('\n'.join(keys))
for required_key in required_keys:
    if required_key not in keys:
        print(f'Required ROOT object key not found {required_key}')
        syst.exit(1)


expected_integral_pt_1 = 222.88716647028923

# test value of the integral of the ggH_pt_1 histogram
# check if difference is a small number to allow for rounding effects
integral = file.ggH_pt_1.Integral()
if abs(integral-expected_integral_pt_1) > 0.0001:
    print(f'Integral of ggH_pt_1 is different: {integral}')
    sys.exit(2)

expected_number_of_bins = 32
assert file.ggH_pt_2.GetNbinsX() == expected_number_of_bins, \
    f'Number of bins of ggH_pt_2 differs from the expected value of {expected_number_of_bins}'
