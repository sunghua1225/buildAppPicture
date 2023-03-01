
import os
import shutil

# 获取当前工作目录的路径
current_dir = os.getcwd()
# 获取当前工作目录的文件夹名
current_folder = os.path.basename(current_dir)

# 定义原始文件夹和目标文件夹
#  ".\\png_logos\\"
original_folder = ".\\png_logos\\"
original_folder_round = ".\\png_logos(round)"
target_folder = "C:\\Users\\user\\Desktop\\frontend-android\\lib\\account\\src\\"+current_folder+"\\res\\"
target_folder_feature = "C:\\Users\\user\\Desktop\\frontend-android\\feature\\launcher\\app\\src\\"+current_folder+"\\res\\"

# 定义原始文件名和目标文件名
original_filename = ["32x32.png","36x36.png","72x72.png","96x96.png","144x144.png", "192x192.png","1080x1920.png"]
filename = ["drawable-mdpi","drawable-xhdpi","drawable-xxhdpi","drawable-xxxhdpi"]
filename_feature =["mipmap-hdpi","mipmap-ldpi","mipmap-mdpi","mipmap-xhdpi","mipmap-xxhdpi","mipmap-xxxhdpi","drawable-xxxhdpi"]
target_ic_launcher3 = "ic_launcher3.png"
target_ic_launcher_round = "ic_launcher_round.png"



# 创建目标文件夹（如果不存在）
if not os.path.exists(target_folder):
    os.mkdir("C:\\Users\\user\\Desktop\\frontend-android\\lib\\account\\src\\"+current_folder)
    os.mkdir(target_folder)
    os.mkdir(target_folder+filename[0])
    os.mkdir(target_folder+filename[1])
    os.mkdir(target_folder+filename[2])
    os.mkdir(target_folder+filename[3])
if not os.path.exists(target_folder_feature):
    os.mkdir("C:\\Users\\user\\Desktop\\frontend-android\\feature\\launcher\\app\\src\\"+current_folder)
    os.mkdir(target_folder_feature)
    os.mkdir(target_folder_feature+filename_feature[0])
    os.mkdir(target_folder_feature+filename_feature[1])
    os.mkdir(target_folder_feature+filename_feature[2])
    os.mkdir(target_folder_feature+filename_feature[3])
    os.mkdir(target_folder_feature+filename_feature[4])
    os.mkdir(target_folder_feature+filename_feature[5])
    os.mkdir(target_folder_feature+filename_feature[6])


# 构建原始文件路径和目标文件路径
original_file_path = os.path.join(original_folder, original_filename[2])
target_file_path = os.path.join(target_folder+filename[0])

# 复制文件到目标文件夹
shutil.copy(original_file_path, target_file_path)
shutil.copy(os.path.join(original_folder, original_filename[3]), os.path.join(target_folder+filename[1]))
shutil.copy(os.path.join(original_folder, original_filename[4]), os.path.join(target_folder+filename[2]))
shutil.copy(os.path.join(original_folder, original_filename[5]), os.path.join(target_folder+filename[3]))
# 重命名文件
os.rename(os.path.join(target_folder+filename[0], original_filename[2]), os.path.join(target_folder+filename[0], target_ic_launcher3))
os.rename(os.path.join(target_folder+filename[1], original_filename[3]), os.path.join(target_folder+filename[1], target_ic_launcher3))
os.rename(os.path.join(target_folder+filename[2], original_filename[4]), os.path.join(target_folder+filename[2], target_ic_launcher3))
os.rename(os.path.join(target_folder+filename[3], original_filename[5]), os.path.join(target_folder+filename[3], target_ic_launcher3))

# 复制文件到目标文件夹
shutil.copy(os.path.join(original_folder_round, original_filename[2]), os.path.join(target_folder+filename[0]))
shutil.copy(os.path.join(original_folder_round, original_filename[3]), os.path.join(target_folder+filename[1]))
shutil.copy(os.path.join(original_folder_round, original_filename[4]), os.path.join(target_folder+filename[2]))
shutil.copy(os.path.join(original_folder_round, original_filename[5]), os.path.join(target_folder+filename[3]))
# 重命名文件
os.rename(os.path.join(target_folder+filename[0], original_filename[2]), os.path.join(target_folder+filename[0], target_ic_launcher_round))
os.rename(os.path.join(target_folder+filename[1], original_filename[3]), os.path.join(target_folder+filename[1], target_ic_launcher_round))
os.rename(os.path.join(target_folder+filename[2], original_filename[4]), os.path.join(target_folder+filename[2], target_ic_launcher_round))
os.rename(os.path.join(target_folder+filename[3], original_filename[5]), os.path.join(target_folder+filename[3], target_ic_launcher_round))



#處理feature
shutil.copy(os.path.join(original_folder, original_filename[0]), os.path.join(target_folder_feature+filename_feature[0]))
shutil.copy(os.path.join(original_folder, original_filename[1]), os.path.join(target_folder_feature+filename_feature[1]))
shutil.copy(os.path.join(original_folder, original_filename[2]), os.path.join(target_folder_feature+filename_feature[2]))
shutil.copy(os.path.join(original_folder, original_filename[3]), os.path.join(target_folder_feature+filename_feature[3]))
shutil.copy(os.path.join(original_folder, original_filename[4]), os.path.join(target_folder_feature+filename_feature[4]))
shutil.copy(os.path.join(original_folder, original_filename[5]), os.path.join(target_folder_feature+filename_feature[5]))
os.rename(os.path.join(target_folder_feature+filename_feature[0], original_filename[0]), os.path.join(target_folder_feature+filename_feature[0], target_ic_launcher3))
os.rename(os.path.join(target_folder_feature+filename_feature[1], original_filename[1]), os.path.join(target_folder_feature+filename_feature[1], target_ic_launcher3))
os.rename(os.path.join(target_folder_feature+filename_feature[2], original_filename[2]), os.path.join(target_folder_feature+filename_feature[2], target_ic_launcher3))
os.rename(os.path.join(target_folder_feature+filename_feature[3], original_filename[3]), os.path.join(target_folder_feature+filename_feature[3], target_ic_launcher3))
os.rename(os.path.join(target_folder_feature+filename_feature[4], original_filename[4]), os.path.join(target_folder_feature+filename_feature[4], target_ic_launcher3))
os.rename(os.path.join(target_folder_feature+filename_feature[5], original_filename[5]), os.path.join(target_folder_feature+filename_feature[5], target_ic_launcher3))


shutil.copy(os.path.join(original_folder_round, original_filename[0]), os.path.join(target_folder_feature+filename_feature[0]))
shutil.copy(os.path.join(original_folder_round, original_filename[1]), os.path.join(target_folder_feature+filename_feature[1]))
shutil.copy(os.path.join(original_folder_round, original_filename[2]), os.path.join(target_folder_feature+filename_feature[2]))
shutil.copy(os.path.join(original_folder_round, original_filename[3]), os.path.join(target_folder_feature+filename_feature[3]))
shutil.copy(os.path.join(original_folder_round, original_filename[4]), os.path.join(target_folder_feature+filename_feature[4]))
shutil.copy(os.path.join(original_folder_round, original_filename[5]), os.path.join(target_folder_feature+filename_feature[5]))
os.rename(os.path.join(target_folder_feature+filename_feature[0], original_filename[0]), os.path.join(target_folder_feature+filename_feature[0], target_ic_launcher_round))
os.rename(os.path.join(target_folder_feature+filename_feature[1], original_filename[1]), os.path.join(target_folder_feature+filename_feature[1], target_ic_launcher_round))
os.rename(os.path.join(target_folder_feature+filename_feature[2], original_filename[2]), os.path.join(target_folder_feature+filename_feature[2], target_ic_launcher_round))
os.rename(os.path.join(target_folder_feature+filename_feature[3], original_filename[3]), os.path.join(target_folder_feature+filename_feature[3], target_ic_launcher_round))
os.rename(os.path.join(target_folder_feature+filename_feature[4], original_filename[4]), os.path.join(target_folder_feature+filename_feature[4], target_ic_launcher_round))
os.rename(os.path.join(target_folder_feature+filename_feature[5], original_filename[5]), os.path.join(target_folder_feature+filename_feature[5], target_ic_launcher_round))



shutil.copy(os.path.join(".\\", original_filename[6]), os.path.join(target_folder_feature+filename_feature[6]))
os.rename(os.path.join(target_folder_feature+filename_feature[6], original_filename[6]), os.path.join(target_folder_feature+filename_feature[6], "bg_splash_center3.png"))