import os
import shutil
import re
import sys

def sampling_data_files(src_dir, dst_dir, step):
    # source directory에 있는 모든 파일 이름을 불러오기
    org_files = os.listdir(src_dir)

    # Regular Expression을 통해 'frame_(number)' 부분만 추출
    pattern = re.compile(r'depth_(\d+)')

    for file in org_files:
        if file.endswith('.png'):
            # Regular Expression을 통해 숫자 추출
            match = pattern.search(file)
            if match:
                try:
                    # 추출된 숫자를 정수로 반환
                    number = int(match.group(1))

                    # 사용자가 지정한 배수에 해당하는 파일만 선택
                    if number % step == 0:
                        src_path = os.path.join(src_dir, file)
                        dst_path = os.path.join(dst_dir, file)

                        shutil.copy(src_path, dst_path)

                except ValueError:
                    pass

if __name__ == '__main__':
    _, src_dir, dst_dir = sys.argv

    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    step = int(input("Enter the step size for sampling (e.g., 2 for every 2nd file) : "))
    sampling_data_files(src_dir, dst_dir, step)

