# Open3D: www.open3d.org
# The MIT License (MIT)
# See license file or visit www.open3d.org for details

# examples/Python/Tutorial/Advanced/fast_global_registration.py

from open3d import *
from global_registration import *
import numpy as np
import copy
import argparse

import time

def execute_fast_global_registration(source_down, target_down,
        source_fpfh, target_fpfh, voxel_size):
    distance_threshold = voxel_size * 0.5
    print(":: Apply fast global registration with distance threshold %.3f" \
            % distance_threshold)
    result = registration_fast_based_on_feature_matching(
            source_down, target_down, source_fpfh, target_fpfh,
            FastGlobalRegistrationOption(
            maximum_correspondence_distance = distance_threshold))
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--source-path', required=True)
    parser.add_argument('--target-path', required=True)
    parser.add_argument('--voxel-size', required=False, default=0.05)
    parser.add_argument('--output-path', required=False, default='./transform.npy')
    args = parser.parse_args()
    voxel_size = float(args.voxel_size)
    source, target, source_down, target_down, source_fpfh, target_fpfh = \
            prepare_dataset(voxel_size, args.source_path, args.target_path)

    start = time.time()
    result_fast = execute_fast_global_registration(source_down, target_down,
            source_fpfh, target_fpfh, voxel_size)
    print("Fast global registration took %.3f sec.\n" % (time.time() - start))
    print(result_fast)
    np.save(args.output_path, np.array(result_fast.transformation))
