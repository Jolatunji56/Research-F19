(base) joshua@toronto:~$ cd /home/shared/data
(base) joshua@toronto:/home/shared/data$ python
Python 2.7.16 |Anaconda, Inc.| (default, Mar 14 2019, 21:00:58) 
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import pynbody
>>> import pylab
>>> s = pynbody.load('/home/shared/data/h148/h148.cosmo50PLK.3072g3HbwK1BH.004096/h148.cosmo50PLK.3072g3HbwK1BH.004096')
>>> h = s.halos()
>>> h1 = h[1]
>>> print('ngas = %e, ndark = %e, nstar = %e\n'%(len(h1.gas),len(h1.dark),len(h1.star)))
ngas = 6.774685e+06, ndark = 4.136782e+07, nstar = 3.689990e+07

>>> pynbody.analysis.halo.center(h1,mode='hyb')
<pynbody.transformation.GenericTranslation object at 0x7f332a276510>
>>> print(h[1]['pos'][0])
[-0.00384686 -0.00104321 -0.00245482]
>>> print(h[5]['pos'][0])
[ 0.00285176  0.00361832 -0.00176657]
>>> h5 = h[5]
>>> my_h5_transformation = pynbody.analysis.halo.center(h5, mode='hyb', move_all=False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/joshua/anaconda2/lib/python2.7/site-packages/pynbody/analysis/halo.py", line 331, in center
    velc = vel_center(sim, cen_size=cen_size, retcen=True)
  File "/home/joshua/anaconda2/lib/python2.7/site-packages/pynbody/analysis/halo.py", line 247, in vel_center
    raise ValueError, "Insufficient particles around center to get velocity"
ValueError: Insufficient particles around center to get velocity
>>> print(h[1]['pos'][0])
[-0.00384686 -0.00104321 -0.00245482]
>>> s.physical_units()
>>> pynbody.plot.image(h1.g, width=100, cmap='Blues')
QApplication: invalid style override passed, ignoring it.
SimArray([[4736.1245, 4747.075 , 4758.0254, ..., 6767.5586, 6758.6924,
           6749.825 ],
          [4703.792 , 4710.217 , 4716.6416, ..., 6791.8467, 6797.055 ,
           6802.264 ],
          [4671.46  , 4673.3584, 4675.257 , ..., 6816.1343, 6835.4194,
           6854.703 ],
          ...,
          [9576.683 , 9497.702 , 9418.722 , ..., 7001.5693, 7116.0854,
           7230.599 ],
          [9596.977 , 9511.9   , 9426.824 , ..., 6972.344 , 7086.055 ,
           7199.7646],
          [9617.2705, 9526.1   , 9434.928 , ..., 6943.12  , 7056.025 ,
           7168.93  ]], dtype=float32, 'Msol kpc**-3')
>>> plt.show()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'plt' is not defined
>>> import matplotlib.pylab as plt
>>> plt.show()

