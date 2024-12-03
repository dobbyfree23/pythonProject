'''
Ex12-3-module.py

as 키워드 별명 사용하기 (alias)
'''

import converter as cvt
from converter import kilometer_to_miles as k_to_m

miles = cvt.kilometer_to_miles(150)
print(f'150km = {miles}miles')

miles2 = k_to_m(150)
print(f'150km = {miles2}miles')



