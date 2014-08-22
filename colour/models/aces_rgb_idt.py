#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ACES RGB Colourspace - Input Device Transform
=============================================

Defines the *ACES RGB* colourspace *Input Device Transform* utilities:

-   :func:`spectral_to_aces_relative_exposure_values`

References
----------
.. [1]  http://www.oscars.org/science-technology/council/projects/aces.html
        (Last accessed 24 February 2014)
.. [2]  http://www.dropbox.com/sh/iwd09buudm3lfod/gyjDF-k7oC/ACES_v1.0.1.pdf
        (Last accessed 24 February 2014)
"""

from __future__ import division, unicode_literals

import numpy as np

from colour.colorimetry import ILLUMINANTS_RELATIVE_SPDS
from colour.models import ACES_RICD

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2014 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['FLARE_PERCENTAGE',
           'S_FLARE_FACTOR',
           'spectral_to_aces_relative_exposure_values']

FLARE_PERCENTAGE = 0.00500
S_FLARE_FACTOR = 0.18000 / (0.18000 + FLARE_PERCENTAGE)


def spectral_to_aces_relative_exposure_values(
        spd,
        illuminant=ILLUMINANTS_RELATIVE_SPDS.get('D60')):
    """
    Converts given spectral power distribution to *ACES RGB* colourspace
    relative exposure values.

    Parameters
    ----------
    spd : SpectralPowerDistribution
        Spectral power distribution.
    illuminant : SpectralPowerDistribution, optional
        *Illuminant* spectral power distribution.

    Returns
    -------
    ndarray, (3,)
        *ACES RGB* colourspace relative exposure values matrix.

    Notes
    -----
    -   Output *ACES RGB* colourspace relative exposure values matrix is in
        domain [0, 1].

    See Also
    --------
    :func:`colour.colorimetry.tristimulus.spectral_to_XYZ`

    References
    ----------

    Examples
    --------
    """

    shape = ACES_RICD.shape
    if spd.shape != ACES_RICD.shape:
        spd = spd.clone().align(shape)

    if illuminant.shape != ACES_RICD.shape:
        illuminant = illuminant.clone().align(shape)

    spd = spd.values
    illuminant = illuminant.values

    r_bar, g_bar, b_bar = (ACES_RICD.r_bar.values,
                           ACES_RICD.g_bar.values,
                           ACES_RICD.b_bar.values)

    get_k = lambda x, y: 1 / np.sum(x * y)

    k_r = get_k(illuminant, r_bar)
    k_g = get_k(illuminant, g_bar)
    k_b = get_k(illuminant, b_bar)

    E_r = k_r * np.sum(illuminant * spd * r_bar)
    E_g = k_g * np.sum(illuminant * spd * g_bar)
    E_b = k_b * np.sum(illuminant * spd * b_bar)

    E_rgb = np.array([E_r, E_g, E_b])

    # Accounting for flare.
    E_rgb += FLARE_PERCENTAGE
    E_rgb *= S_FLARE_FACTOR

    return E_rgb
