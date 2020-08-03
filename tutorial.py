from nuscenes.nuscenes import NuScenes
import cv2

nusc = NuScenes(version='v1.02-train', dataroot='/Users/pengfeima/Desktop/Lyft/v1.02-train', verbose=False)

# Render
my_sample = nusc.sample[3]
print(len(nusc.sample))

# point cloud points to image
# nusc.render_pointcloud_in_image(my_sample['token'], pointsensor_channel='LIDAR_TOP',out_path='./render_pc2img.jpg')

# 3d boxes on image
#nusc.render_sample_data(my_sample['data']['CAM_FRONT'], out_path='./render_cam_front.jpg')

# birdeye 
#nusc.render_sample_data(my_sample['data']['LIDAR_TOP'], out_path='./render_lidar_top.jpg',nsweeps=5, underlay_map=True)

'''
# 1. scene
#nusc.list_scenes()
my_scene = nusc.scene[0]


# 2. sample
first_sample_token = my_scene['first_sample_token']
my_sample = nusc.get('sample', first_sample_token)
nusc.list_sample(my_sample['token'])

# 3. sample_data
sensor = 'CAM_FRONT'
cam_front_data = nusc.get('sample_data', my_sample['data'][sensor])
nusc.render_sample_data(cam_front_data['token'], out_path='./render.jpg')

# 4. sample_annotation
my_annotation_token = my_sample['anns'][6]
my_annotation_metadata =  nusc.get('sample_annotation', my_annotation_token)
#my_annotation_metadata

nusc.render_annotation(my_annotation_token, out_path='./render_ann.jpg')

# 5. instance
my_instance = nusc.instance[10]
my_instance
instance_token = my_instance['token']
nusc.render_instance(instance_token, out_path='./render_instance_1.jpg')

print("First annotated sample of this instance:")
nusc.render_annotation(my_instance['first_annotation_token'], out_path='./render_instance_2.jpg')

print("Last annotated sample of this instance")
nusc.render_annotation(my_instance['last_annotation_token'], out_path='./render_instance_3.jpg')



# 6. category
nusc.list_categories()
print(nusc.category[2])



# 7. attribute
nusc.list_attributes()



# 8. visibility
print(nusc.visibility)


# 9. sensor 
print(nusc.sensor)
print(nusc.sample_data[10])


# 10. calibrated_sensor
print(nusc.calibrated_sensor[0])
'''
