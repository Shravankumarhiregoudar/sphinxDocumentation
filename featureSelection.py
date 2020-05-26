from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def RFFeatureSelection(XTrain,yTrain,XTest,yTest,wavelengths):
    """
        :RFFeatureSelection: Random Forest feature selection, Plot the wavelengths vs 
                             Feature Importance for target based on RF on spectral data
        :param xTrain: Train spectral data
        :type xTrain: ndarray

        :param yTrain: Train target data
        :type yTrain: ndarray

        :param xTest: Test spectral data
        :type xTest: ndarray

        :param yTest: Test target data
        :type yTest: ndarray

        :param wavelengths: List denoting wavenumber or wavelength.
        :type wavelengths: list

        :returns: Graph of wavelengths vs Feature Importance for target based on RF on spectral data
    """
    model = RandomForestRegressor(n_estimators = 100,
                                 random_state = 42,
                                 max_features='sqrt').fit(XTrain,yTrain)
    model.score(XTest,yTest)

    imp = model.feature_importances_

    fig, ax = plt.subplots(figsize = (10,10),dpi=150)
    ax.set_xlim(np.min(wavelengths), np.max(wavelengths))
    ax.set_ylim(np.min(imp), np.max(imp))
    plt.scatter(wavelengths,imp)
    plt.title("Feature Importance for target based on RF on spectral data",fontsize=15)
    plt.ylabel("Importance (bigger is more important)",fontsize=12)
    plt.xlabel("Wavelength",fontsize=12)

def impRange(m,n,XTrain,XTest,wavelengths):
    """
        :impRange: Perpares important spectral data based on important wavelength range from the graph generated form 
                   RFFeatureSelection function.
        :param m: Lower limit of important wavelength range
        :type m: int

        :param n: Upper limit of important wavelength range
        :type n: int

        :param XTrain: Train spectral data
        :type XTrain: ndarray

        :param XTest: Test spectral data
        :type XTest: ndarray

        :param wavelengths: List denoting wavenumber or wavelength.
        :type wavelengths: list

        :returns: Important train and test spectral data based on RF feature selection
    """
    # Looking at the above graph enter the max and min of imp wavelengths 
    impWave = [m,n]
    # Find the nearest index of the wavelengths
    impWaveIndex = range(pd.DataFrame(wavelengths).sub(impWave[0]).abs().idxmin()[0],
                   pd.DataFrame(wavelengths).sub(impWave[1]).abs().idxmin()[0])
    # Assign the imp wavelength range to spetral data
    impXTrain = XTrain[:,impWaveIndex]
    impXTest = XTest[:,impWaveIndex]
    return (impXTrain,impXTest)