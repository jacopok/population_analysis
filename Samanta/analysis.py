import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os 


#__________________________
#        Get data
#--------------------------
dictionary = {}


data = np.loadtxt('mergers_Z=1e-4.out', skiprows=1, usecols=range(0,21))[:,[1,2,8,9,10,11,12,13,14]]
lista = ['min1','min2','sepform','eccform','k1form','m1form','k2form','m2form','tmerg']
DF = pd.DataFrame(data, columns = lista)
dictionary['1e-4'] = DF

data_Z2 = np.loadtxt('mergers_Z=2e-2.out', skiprows=1, usecols=range(0,21))[:,[1,2,8,9,10,11,12,13,14]]
DF2 = pd.DataFrame(data_Z2, columns = lista)
dictionary['2e-2'] = DF2
data_Z3 = np.loadtxt('mergers_Z=2e-3.out', skiprows=1, usecols=range(0,21))[:,[1,2,8,9,10,11,12,13,14]]
DF3 = pd.DataFrame(data_Z3, columns = lista)
dictionary['2e-3'] = DF3
data_Z4 = np.loadtxt('mergers_Z=2e-4.out', skiprows=1, usecols=range(0,21))[:,[1,2,8,9,10,11,12,13,14]]
DF4 = pd.DataFrame(data_Z4, columns = lista)
dictionary['2e-4'] = DF4




#_____________________________
#            Plots            
#-----------------------------

plt.scatter(DF.loc[(DF['k1form']==14) & (DF['k2form']==14)]['min1'].values,DF.loc[(DF['k1form']==14) & (DF['k2form']==14)]['m1form'].values, alpha=0.4, label='Primary')
plt.scatter(DF.loc[(DF['k1form']==14) & (DF['k2form']==14)]['min2'].values,DF.loc[(DF['k1form']==14) & (DF['k2form']==14)]['m2form'].values, marker = '*', alpha=0.4,label='Secondary')
plt.grid()
plt.title('Metallicity Z=1e-4')
plt.xlabel('ZAMS masses')
plt.ylabel('Mass of Compact Object')
plt.legend(loc='right')
plt.savefig('Zams_vs_CO_1Z4.png')
plt.clf()

plt.scatter(DF2.loc[(DF2['k1form']==14) & (DF2['k2form']==14)]['min1'].values,DF2.loc[(DF2['k1form']==14) & (DF2['k2form']==14)]['m1form'].values, alpha=0.4, label='Primary')
plt.scatter(DF2.loc[(DF2['k1form']==14) & (DF2['k2form']==14)]['min2'].values,DF2.loc[(DF3['k1form']==14) & (DF2['k2form']==14)]['m2form'].values, marker = '*', alpha=0.4,label='Secondary')
plt.grid()
plt.title('Metallicity Z=2e-2')
plt.xlabel('ZAMS masses')
plt.ylabel('Mass of Compact Object')
plt.legend(loc='right')
plt.savefig('Zams_vs_CO_Z2.png')
plt.clf()

plt.scatter(DF3.loc[(DF3['k1form']==14) & (DF3['k2form']==14)]['min1'].values,DF3.loc[(DF3['k1form']==14) & (DF3['k2form']==14)]['m1form'].values, alpha=0.4, label='Primary')
plt.scatter(DF3.loc[(DF3['k1form']==14) & (DF3['k2form']==14)]['min2'].values,DF3.loc[(DF3['k1form']==14) & (DF3['k2form']==14)]['m2form'].values, marker = '*', alpha=0.4,label='Secondary')
plt.grid()
plt.title('Metallicity Z=2e-3')
plt.xlabel('ZAMS masses')
plt.ylabel('Mass of Compact Object')
plt.legend(loc='right')
plt.savefig('Zams_vs_CO_Z3.png')
plt.clf()

plt.scatter(DF4.loc[(DF4['k1form']==14) & (DF4['k2form']==14)]['min1'].values,DF4.loc[(DF4['k1form']==14) & (DF4['k2form']==14)]['m1form'].values, alpha=0.4, label='Primary')
plt.scatter(DF4.loc[(DF4['k1form']==14) & (DF4['k2form']==14)]['min2'].values,DF4.loc[(DF4['k1form']==14) & (DF4['k2form']==14)]['m2form'].values, marker = '*', alpha=0.4,label='Secondary')
plt.grid()
plt.title('Metallicity Z=2e-4')
plt.xlabel('ZAMS masses')
plt.ylabel('Mass of Compact Object')
plt.legend(loc='right')
plt.savefig('Zams_vs_CO_Z4.png')
plt.clf()

# Histograms

plt.hist(DF.loc[(DF['k1form']==14) & (DF['k2form']==14)]['min1'].values, histtype='step', linestyle=':', label = 'Z=1e-4')
plt.hist(DF2.loc[(DF2['k1form']==14) & (DF2['k2form']==14)]['min1'].values, histtype='step', linestyle='-.', label = 'Z=2e-2')
plt.hist(DF3.loc[(DF3['k1form']==14) & (DF3['k2form']==14)]['min1'].values, histtype='step', linestyle='dashed',label = 'Z=2e-3')
plt.hist(DF4.loc[(DF4['k1form']==14) & (DF4['k2form']==14)]['min1'].values, histtype='step', label = 'Z=2e-4')
plt.xlabel('ZAMS Masses of primary star')
plt.ylabel('Number of mergers')
plt.legend(loc='upper right')
plt.savefig('Zams_masses_primary_histogram.pdf')
plt.clf()

plt.hist(DF.loc[(DF['k1form']==14) & (DF['k2form']==14)]['min2'].values, histtype='step', linestyle=':', label = 'Z=1e-4')
plt.hist(DF2.loc[(DF2['k1form']==14) & (DF2['k2form']==14)]['min2'].values, histtype='step', linestyle='-.', label = 'Z=2e-2')
plt.hist(DF3.loc[(DF3['k1form']==14) & (DF3['k2form']==14)]['min2'].values, histtype='step', linestyle='dashed',label = 'Z=2e-3')
plt.hist(DF4.loc[(DF4['k1form']==14) & (DF4['k2form']==14)]['min2'].values, histtype='step', label = 'Z=2e-4')
plt.xlabel('ZAMS Masses of secondary star')
plt.ylabel('Number of mergers')
plt.legend(loc='upper right')
plt.savefig('Zams_masses_secondary_histogram.pdf')
plt.clf()

#5) Distribution of ecc and semi major axis?

plt.hist(DF.loc[(DF['k1form']==14) & (DF['k2form']==14)]['eccform'].values, histtype='step', linestyle=':', label = 'Z=1e-4')
plt.hist(DF2.loc[(DF2['k1form']==14) & (DF2['k2form']==14)]['eccform'].values, histtype='step', linestyle='-.', label = 'Z=2e-2')
plt.hist(DF3.loc[(DF3['k1form']==14) & (DF3['k2form']==14)]['eccform'].values, histtype='step', linestyle='dashed',label = 'Z=2e-3')
plt.hist(DF4.loc[(DF4['k1form']==14) & (DF4['k2form']==14)]['eccform'].values, histtype='step', label = 'Z=2e-4')
plt.xlabel('Eccentricity of BBH systems')
plt.ylabel('Number of BBH mergers')
plt.legend(loc='upper right')
plt.savefig('Eccentricities_histogram.pdf')
plt.clf()

plt.hist(DF.loc[(DF['k1form']==14) & (DF['k2form']==14)]['sepform'].values, histtype='step', linestyle=':', label = 'Z=1e-4')
plt.hist(DF2.loc[(DF2['k1form']==14) & (DF2['k2form']==14)]['sepform'].values, histtype='step', linestyle='-.', label = 'Z=2e-2')
plt.hist(DF3.loc[(DF3['k1form']==14) & (DF3['k2form']==14)]['sepform'].values, histtype='step', linestyle='dashed',label = 'Z=2e-3')
plt.hist(DF4.loc[(DF4['k1form']==14) & (DF4['k2form']==14)]['sepform'].values, histtype='step', label = 'Z=2e-4')
plt.xlabel('Initial Semi-major axis of BBH systems')
plt.ylabel('Number of BBH mergers')
plt.legend(loc='upper right')
plt.savefig('Semi_major_axis_histogram.pdf')
plt.clf()

#1) Mass Function of BBH

#1) Mass Function

plt.scatter(DF.loc[(DF['k1form']==14) & (DF['k2form']==14)]['min1'].values,DF.loc[(DF['k2form']==14) & (DF['k1form']==14)]['min2'].values, s = .4, alpha =.5, label = 'Z=1e-4')
plt.scatter(DF2.loc[(DF2['k1form']==14) & (DF2['k2form']==14)]['min1'].values,DF2.loc[(DF2['k2form']==14) & (DF2['k1form']==14)]['min2'].values, s = .4, alpha =.5, label = 'Z=2e-2')
plt.scatter(DF3.loc[(DF3['k1form']==14) & (DF3['k2form']==14)]['min1'].values,DF3.loc[(DF3['k2form']==14) & (DF3['k1form']==14)]['min2'].values, s = .4, alpha =.5, label = 'Z=2e-3')
plt.scatter(DF4.loc[(DF4['k1form']==14) & (DF4['k2form']==14)]['min1'].values,DF4.loc[(DF4['k2form']==14) & (DF4['k1form']==14)]['min2'].values, s = .4, alpha =.5, label = 'Z=2e-3')
plt.xlabel('M1')
plt.ylabel('M2')
#plt.legend(loc='upper right')
plt.savefig('mass_function.png')
plt.clf()

#plt.scatter(m1form[(k1form==14) & (k2form==14)],m2form[(k1form==14) & (k2form==14)], label='Z=1e-4')
#plt.scatter(m1form_Z2[(k1form_Z2==14) & (k2form_Z2==14)],m2form_Z2[(k1form_Z2==14) & (k2form_Z2==14)], label='Z=2e-2')
#plt.scatter(m1form_Z3[(k1form_Z3==14) & (k2form_Z3==14)],m2form_Z3[(k1form_Z3==14) & (k2form_Z3==14)], label='Z=2e-3')
#plt.scatter(m1form_Z4[(k1form_Z4==14) & (k2form_Z4==14)],m2form_Z4[(k1form_Z4==14) & (k2form_Z4==14)], label='Z=2e-4')
#plt.legend(loc='upper right')
#plt.xlabel('m1form')
#plt.ylabel('m2form')
#plt.show()


#3) Distribution of tmerg

plt.hist(DF.loc[(DF['k1form']==14) & (DF['k2form']==14)]['tmerg'].values, histtype='step', linestyle=':', label = 'Z=1e-4')
plt.hist(DF2.loc[(DF2['k1form']==14) & (DF2['k2form']==14)]['tmerg'].values, histtype='step', linestyle='-.', label = 'Z=2e-2')
plt.hist(DF3.loc[(DF3['k1form']==14) & (DF3['k2form']==14)]['tmerg'].values, histtype='step', linestyle='dashed',label = 'Z=2e-3')
plt.hist(DF4.loc[(DF4['k1form']==14) & (DF4['k2form']==14)]['tmerg'].values, histtype='step', label = 'Z=2e-4')
plt.xlabel('Delay Times')
plt.ylabel('Number of BBH mergers')
plt.legend(loc='upper right')
plt.savefig('tmerg_histogram.pdf')
plt.clf()



#plt.scatter(ecc, BBH, label = 'Z=1e-4')
#plt.xlabel('Eccentricity')
#plt.ylabel('BBH total mass')
#plt.show()

#plt.scatter(tmerg[(k1form==14) & (k2form==14)], ecc, label = 'Z=1e-4')
#plt.xlabel('Merger Time')
#plt.ylabel('Eccentricity')
#plt.show()

