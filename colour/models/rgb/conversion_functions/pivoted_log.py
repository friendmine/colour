#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pivoted Log Encoding
====================

Defines the *Pivoted Log* encoding:

-   :def:`log_encoding_PivotedLog`
-   :def:`log_decoding_PivotedLog`

See Also
--------
`RGB Colourspaces IPython Notebook
<http://nbviewer.ipython.org/github/colour-science/colour-ipython/\
blob/master/notebooks/models/rgb.ipynb>`_

References
----------
.. [1]  Sony Imageworks. (2012). make.py. Retrieved November 27, 2014, from
        https://github.com/imageworks/OpenColorIO-Configs/\
blob/master/nuke-default/make.py
"""

from __future__ import division, unicode_literals

import numpy as np

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2015 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['log_encoding_PivotedLog',
           'log_decoding_PivotedLog']


def log_encoding_PivotedLog(value,
                            log_reference=445,
                            linear_reference=0.18,
                            negative_gamma=0.6,
                            density_per_code_value=0.002):
    """
    Defines the *Josh Pines* style *Pivoted Log* log encoding curve /
    opto-electronic conversion function.

    Parameters
    ----------
    value : numeric or array_like
        *Linear* value.
    log_reference : numeric or array_like
        Log reference.
    linear_reference : numeric or array_like
        Linear reference.
    negative_gamma : numeric or array_like
        Negative gamma.
    density_per_code_value : numeric or array_like
        Density per code value.

    Returns
    -------
    numeric or ndarray
        *Josh Pines* style pivoted log value.

    Examples
    --------
    >>> log_encoding_PivotedLog(0.18)  # doctest: +ELLIPSIS
    0.4349951...
    """

    value = np.asarray(value)

    return ((log_reference + np.log10(value / linear_reference) /
             (density_per_code_value / negative_gamma)) / 1023)


def log_decoding_PivotedLog(value,
                            log_reference=445,
                            linear_reference=0.18,
                            negative_gamma=0.6,
                            density_per_code_value=0.002):
    """
    Defines the *Josh Pines* style *Pivoted Log* log decoding curve /
    electro-optical conversion function.

    Parameters
    ----------
    value : numeric or array_like
        *Josh Pines* style pivoted log value.
    log_reference : numeric or array_like
        Log reference.
    linear_reference : numeric or array_like
        Linear reference.
    negative_gamma : numeric or array_like
        Negative gamma.
    density_per_code_value : numeric or array_like
        Density per code value.

    Returns
    -------
    numeric or ndarray
        *Linear* value.

    Examples
    --------
    >>> log_decoding_PivotedLog(0.43499511241446726)  # doctest: +ELLIPSIS
    0.1...
    """

    value = np.asarray(value)

    return (10 ** ((value * 1023 - log_reference) *
                   (density_per_code_value / negative_gamma)) *
            linear_reference)
