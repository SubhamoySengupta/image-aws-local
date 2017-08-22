import upload_from_local
import sync_buckets
import hyve_resize


# STEP-->1 First delete files in S3 bucket hyve-store not present in the bucket hyve-rootwork
# sync_buckets.run()

# STEP-->2 Second reduce size of local images if their height/width is very large
# hyve_resize.resizer.run_8()

# STEP-->3 Third sync local drive and S3 bucket hyve-rootwork
# STEP-->4 Fourth start Iron worker upload the successful and verified files to hyve-store from hyve-rootwork
upload_from_local.scan_dir.run_8()
print 'All tasks completed'
