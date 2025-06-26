import open3d as o3d

CAPTURE_DIR = "/home/borg/borg_ros/captures/"

# Read a PLY file containing a point cloud
pcd = o3d.io.read_point_cloud(CAPTURE_DIR + "pointcloud_20250626_013859.ply")

# You can then visualize or process the point cloud
o3d.visualization.draw_geometries([pcd])