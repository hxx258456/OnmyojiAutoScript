from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class HyakkiyakouAssets: 


	# Click Rule Assets
	# description 
	C_HSELECT_1 = RuleClick(roi_front=(158,209,225,405), roi_back=(158,209,225,405), name="hselect_1")
	# description 
	C_HSELECT_2 = RuleClick(roi_front=(531,225,202,363), roi_back=(531,225,202,363), name="hselect_2")
	# description 
	C_HSELECT_3 = RuleClick(roi_front=(875,210,219,394), roi_back=(875,210,219,394), name="hselect_3")


	# Image Rule Assets
	# 邀请按钮 
	I_HINVITE = RuleImage(roi_front=(139,569,63,60), roi_back=(139,569,63,60), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_hinvite.png")
	# 进入 
	I_HACCESS = RuleImage(roi_front=(1059,554,100,100), roi_back=(1059,554,100,100), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_haccess.png")
	# 开始 
	I_HSTART = RuleImage(roi_front=(1119,555,100,100), roi_back=(1119,555,100,100), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_hstart.png")
	# 押注 
	I_HSELECTED = RuleImage(roi_front=(980,265,41,44), roi_back=(226,53,836,348), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_hselected.png")
	# 结束 
	I_HEND = RuleImage(roi_front=(81,164,86,299), roi_back=(81,164,86,299), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_hend.png")
	# 冰冻 
	I_HFREEZE = RuleImage(roi_front=(1092,665,187,54), roi_back=(1092,665,187,54), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_hfreeze.png")


	# Click Rule Assets
	# description 
	C_CLICK = RuleClick(roi_front=(26,250,33,100), roi_back=(26,250,33,100), name="click")


	# Image Rule Assets
	# 缘结之庭 
	I_TPAGE_1 = RuleImage(roi_front=(238,504,221,123), roi_back=(121,480,950,166), threshold=0.7, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tpage_1.png")
	# 本丸御殿 
	I_TPAGE_2 = RuleImage(roi_front=(411,506,231,120), roi_back=(132,479,933,171), threshold=0.5, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tpage_2.png")
	# 之境 
	I_TPAGE_3 = RuleImage(roi_front=(748,504,240,118), roi_back=(125,482,937,166), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tpage_3.png")
	# 鲸歌潜岸 
	I_TPAGE_4 = RuleImage(roi_front=(281,507,233,120), roi_back=(124,484,933,163), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tpage_4.png")
	# 杨帆远航 
	I_TPAGE_5 = RuleImage(roi_front=(539,506,238,120), roi_back=(130,483,940,166), threshold=0.7, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tpage_5.png")
	# 繁影留住 
	I_TPAGE_6 = RuleImage(roi_front=(801,505,232,118), roi_back=(128,493,937,153), threshold=0.7, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tpage_6.png")
	# description 
	I_TCHECK_1 = RuleImage(roi_front=(19,246,100,100), roi_back=(2,218,135,215), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tcheck_1.png")
	# description 
	I_TCHECK_2 = RuleImage(roi_front=(9,216,157,226), roi_back=(0,197,186,263), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tcheck_2.png")
	# description 
	I_TCHECK_3 = RuleImage(roi_front=(5,126,138,299), roi_back=(2,110,147,345), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tcheck_3.png")
	# description 
	I_TCHECK_4 = RuleImage(roi_front=(7,108,100,332), roi_back=(0,101,120,347), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tcheck_4.png")
	# description 
	I_TCHECK_5 = RuleImage(roi_front=(132,28,77,103), roi_back=(94,13,152,234), threshold=0.4, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tcheck_5.png")
	# description 
	I_TCHECK_6 = RuleImage(roi_front=(9,107,100,350), roi_back=(3,97,113,369), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tcheck_6.png")
	# description 
	I_SWITCH_BACKGROUND = RuleImage(roi_front=(992,649,105,36), roi_back=(969,627,152,72), threshold=0.7, method="Template matching", file="./tasks/Hyakkiyakou/train/train_switch_background.png")
	# description 
	I_TCHECK_22 = RuleImage(roi_front=(14,150,100,100), roi_back=(5,139,124,127), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tcheck_22.png")
	# description 
	I_TCHECK_32 = RuleImage(roi_front=(35,175,100,100), roi_back=(26,155,123,141), threshold=0.7, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tcheck_32.png")
	# 检查是否在砸豆子 
	I_CHECK_RUN = RuleImage(roi_front=(95,598,92,45), roi_back=(68,578,143,100), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/train/train_check_run.png")


	# Swipe Rule Assets
	# description 
	S_TSWIPE = RuleSwipe(roi_front=(421,521,21,91), roi_back=(273,516,23,100), mode="default", name="tswipe")
	# description 
	S_TBACK = RuleSwipe(roi_front=(259,515,21,100), roi_back=(993,521,22,100), mode="default", name="tback")


