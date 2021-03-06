# -*- coding: utf-8 -*-
"""
Illuminants
===========

Defines *CIE* illuminants computation related objects:

-   :func:`colour.D_illuminant_relative_spd`
-   :func:`colour.CIE_standard_illuminant_A_function`

See Also
--------
`Illuminants Jupyter Notebook
<http://nbviewer.jupyter.org/github/colour-science/colour-notebooks/\
blob/master/notebooks/colorimetry/illuminants.ipynb>`_

References
----------
-   :cite:`CIETC1-482004` CIE TC 1-48. (2004). EXPLANATORY COMMENTS - 5. In
    CIE 015:2004 Colorimetry, 3rd Edition (pp. 68-68). ISBN:978-3-901-90633-6
-   :cite:`CIETC1-482004n` : CIE TC 1-48. (2004). 3.1 Recommendations
    concerning standard physical data of illuminants. In CIE 015:2004
    Colorimetry, 3rd Edition (pp. 12-13). ISBN:978-3-901-90633-6
-   :cite:`Wyszecki2000z` : Wyszecki, G., & Stiles, W. S. (2000). CIE Method of
    Calculating D-Illuminants. In Color Science: Concepts and Methods,
    Quantitative Data and Formulae (pp. 145-146). Wiley. ISBN:978-0471399186
"""

from __future__ import division, unicode_literals

import numpy as np

from colour.colorimetry import D_ILLUMINANTS_S_SPDS, SpectralPowerDistribution
from colour.utilities import as_float_array, tsplit

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2018 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['D_illuminant_relative_spd', 'CIE_standard_illuminant_A_function']


def D_illuminant_relative_spd(xy, M1_M2_rounding=True):
    """
    Returns the relative spectral power distribution of given
    *CIE Standard Illuminant D Series* using given *xy* chromaticity
    coordinates.

    Parameters
    ----------
    xy : array_like
        *xy* chromaticity coordinates.
    M1_M2_rounding : bool, optional
        Whether to round :math:`M1` and :math:`M2` variables to 3 decimal
        places in order to yield the internationally agreed values.

    Returns
    -------
    SpectralPowerDistribution
        *CIE Standard Illuminant D Series* relative spectral power
        distribution.

    Notes
    -----
    -   The nominal *xy* chromaticity coordinates which have been computed with
        :func:`colour.temperature.CCT_to_xy_CIE_D` must be given according to
        *CIE 015:2004* recommendation and thus multiplied by 1.4388 / 1.4380.
    -   :math:`M1` and :math:`M2` variables are rounded to 3 decimal places
         according to *CIE 015:2004* recommendation.

    References
    ----------
    :cite:`CIETC1-482004`, :cite:`Wyszecki2000z`

    Examples
    --------
    >>> from colour.utilities import numpy_print_options
    >>> from colour.temperature import CCT_to_xy_CIE_D
    >>> CCT_D65 = 6500 * 1.4388 / 1.4380
    >>> xy = CCT_to_xy_CIE_D(CCT_D65)
    >>> with numpy_print_options(suppress=True):
    ...     D_illuminant_relative_spd(xy)  # doctest: +ELLIPSIS
    SpectralPowerDistribution([[ 300.     ,    0.0341...],
                               [ 305.     ,    1.6643...],
                               [ 310.     ,    3.2945...],
                               [ 315.     ,   11.7652...],
                               [ 320.     ,   20.236 ...],
                               [ 325.     ,   28.6447...],
                               [ 330.     ,   37.0535...],
                               [ 335.     ,   38.5011...],
                               [ 340.     ,   39.9488...],
                               [ 345.     ,   42.4302...],
                               [ 350.     ,   44.9117...],
                               [ 355.     ,   45.775 ...],
                               [ 360.     ,   46.6383...],
                               [ 365.     ,   49.3637...],
                               [ 370.     ,   52.0891...],
                               [ 375.     ,   51.0323...],
                               [ 380.     ,   49.9755...],
                               [ 385.     ,   52.3118...],
                               [ 390.     ,   54.6482...],
                               [ 395.     ,   68.7015...],
                               [ 400.     ,   82.7549...],
                               [ 405.     ,   87.1204...],
                               [ 410.     ,   91.486 ...],
                               [ 415.     ,   92.4589...],
                               [ 420.     ,   93.4318...],
                               [ 425.     ,   90.0570...],
                               [ 430.     ,   86.6823...],
                               [ 435.     ,   95.7736...],
                               [ 440.     ,  104.8649...],
                               [ 445.     ,  110.9362...],
                               [ 450.     ,  117.0076...],
                               [ 455.     ,  117.4099...],
                               [ 460.     ,  117.8122...],
                               [ 465.     ,  116.3365...],
                               [ 470.     ,  114.8609...],
                               [ 475.     ,  115.3919...],
                               [ 480.     ,  115.9229...],
                               [ 485.     ,  112.3668...],
                               [ 490.     ,  108.8107...],
                               [ 495.     ,  109.0826...],
                               [ 500.     ,  109.3545...],
                               [ 505.     ,  108.5781...],
                               [ 510.     ,  107.8017...],
                               [ 515.     ,  106.2957...],
                               [ 520.     ,  104.7898...],
                               [ 525.     ,  106.2396...],
                               [ 530.     ,  107.6895...],
                               [ 535.     ,  106.0475...],
                               [ 540.     ,  104.4055...],
                               [ 545.     ,  104.2258...],
                               [ 550.     ,  104.0462...],
                               [ 555.     ,  102.0231...],
                               [ 560.     ,  100.    ...],
                               [ 565.     ,   98.1671...],
                               [ 570.     ,   96.3342...],
                               [ 575.     ,   96.0611...],
                               [ 580.     ,   95.788 ...],
                               [ 585.     ,   92.2368...],
                               [ 590.     ,   88.6856...],
                               [ 595.     ,   89.3459...],
                               [ 600.     ,   90.0062...],
                               [ 605.     ,   89.8026...],
                               [ 610.     ,   89.5991...],
                               [ 615.     ,   88.6489...],
                               [ 620.     ,   87.6987...],
                               [ 625.     ,   85.4936...],
                               [ 630.     ,   83.2886...],
                               [ 635.     ,   83.4939...],
                               [ 640.     ,   83.6992...],
                               [ 645.     ,   81.863 ...],
                               [ 650.     ,   80.0268...],
                               [ 655.     ,   80.1207...],
                               [ 660.     ,   80.2146...],
                               [ 665.     ,   81.2462...],
                               [ 670.     ,   82.2778...],
                               [ 675.     ,   80.281 ...],
                               [ 680.     ,   78.2842...],
                               [ 685.     ,   74.0027...],
                               [ 690.     ,   69.7213...],
                               [ 695.     ,   70.6652...],
                               [ 700.     ,   71.6091...],
                               [ 705.     ,   72.9790...],
                               [ 710.     ,   74.349 ...],
                               [ 715.     ,   67.9765...],
                               [ 720.     ,   61.604 ...],
                               [ 725.     ,   65.7448...],
                               [ 730.     ,   69.8856...],
                               [ 735.     ,   72.4863...],
                               [ 740.     ,   75.087 ...],
                               [ 745.     ,   69.3398...],
                               [ 750.     ,   63.5927...],
                               [ 755.     ,   55.0054...],
                               [ 760.     ,   46.4182...],
                               [ 765.     ,   56.6118...],
                               [ 770.     ,   66.8054...],
                               [ 775.     ,   65.0941...],
                               [ 780.     ,   63.3828...],
                               [ 785.     ,   63.8434...],
                               [ 790.     ,   64.304 ...],
                               [ 795.     ,   61.8779...],
                               [ 800.     ,   59.4519...],
                               [ 805.     ,   55.7054...],
                               [ 810.     ,   51.959 ...],
                               [ 815.     ,   54.6998...],
                               [ 820.     ,   57.4406...],
                               [ 825.     ,   58.8765...],
                               [ 830.     ,   60.3125...]],
                              interpolator=SpragueInterpolator,
                              interpolator_args={},
                              extrapolator=Extrapolator,
                              extrapolator_args={...})
    """

    x, y = tsplit(xy)

    M = 0.0241 + 0.2562 * x - 0.7341 * y
    M1 = (-1.3515 - 1.7703 * x + 5.9114 * y) / M
    M2 = (0.0300 - 31.4424 * x + 30.0717 * y) / M

    if M1_M2_rounding:
        M1 = np.around(M1, 3)
        M2 = np.around(M2, 3)

    S0 = D_ILLUMINANTS_S_SPDS['S0']
    S1 = D_ILLUMINANTS_S_SPDS['S1']
    S2 = D_ILLUMINANTS_S_SPDS['S2']

    distribution = S0.values + M1 * S1.values + M2 * S2.values

    return SpectralPowerDistribution(
        distribution, S0.wavelengths, name='CIE Standard Illuminant D Series')


def CIE_standard_illuminant_A_function(wl):
    """
    *CIE Standard Illuminant A* is intended to represent typical, domestic,
    tungsten-filament lighting.

    Its relative spectral power distribution is that of a Planckian radiator
    at a temperature of approximately 2856 K. *CIE Standard Illuminant A*
    should be used in all applications of colorimetry involving the use of
    incandescent lighting, unless there are specific reasons for using
    a different illuminant.

    Parameters
    ----------
    wl : array_like
        Wavelength to evaluate the function at.

    Returns
    -------
    ndarray
        *CIE Standard Illuminant A* value at given wavelength.

    References
    ----------
    :cite:`CIETC1-482004n`

    Examples
    --------
    >>> wl = np.array([560, 580, 581.5])
    >>> CIE_standard_illuminant_A_function(wl)  # doctest: +ELLIPSIS
    array([ 100.        ,  114.4363383...,  115.5285063...])
    """

    wl = as_float_array(wl)

    return (100 * (560 / wl) ** 5 * (((np.exp(
        (1.435 * 10 ** 7) / (2848 * 560)) - 1) / (np.exp(
            (1.435 * 10 ** 7) / (2848 * wl)) - 1))))
