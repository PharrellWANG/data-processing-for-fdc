This directory contains PDFs for edge distributions
===================================================

Algorithm for calculating edge strength of a block
--------------------------------------------------

block strength ``ave`` seldom larger than 20000 except in DMM1, VERTICAL(26), HORIZONTAL(10), DMM4

.. code-block:: python

            features, label = row[:-1], row[-1]
            features = features.reshape(RESHAPE, RESHAPE)
            for i in range(RESHAPE - 1):
                for j in range(RESHAPE - 1):
                    horizontal_strength = \
                        features[i][j] + \
                        features[i + 1][j] - \
                        features[i][j + 1] - \
                        features[i + 1][j + 1]
                    vertical_strength = \
                        features[i][j] + \
                        features[i][j + 1] - \
                        features[i + 1][j] - \
                        features[i + 1][j + 1]
                    strength = horizontal_strength ** 2 + vertical_strength ** 2
                    # total strength of a block (or you can say a line in the csv file)
                    data = np.append(data, np.array([strength]))
                    total_strength += strength

            assert (data.ndim == 1)
            # top RESHAPE*2 && non-zero average.
            # step1: top RESHAPE*2 values in the numpy arrary (let k == RESHAPE*2)
            top_k = data[np.argsort(data)][data.size - RESHAPE * 2:]
            assert (top_k.ndim == 1)
            # step2: non-zero values (because sometimes the edge length can be short. We only want the sharpness. We do not want smooth regions to affect the sharpness.)
            data = top_k[top_k.nonzero()]
            data = data[np.where(data > 8)]  # for [[2, 0], [0, 0]], i exclude it from the concept of sharp
            if data.size == 0:  # all the strength are zero. (that is to say , it is the DC mode)
                ave = 0
                data = np.array([0])
            else:
                ave = np.mean(data)
                data = np.array([ave])

