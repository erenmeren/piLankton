#!/usr/bin/python3

import time
import boto3
from botocore.exceptions import ClientError
from draw import Draw

class AWS:

  AWS_S3_BUCKET = 'eprint-test'
  AWS_S3_FOLDER = 'jimmy_and_the_bee/'
  FILE_NAME = 'receipt.raw'

  # aws s3
  s3 = boto3.resource('s3')
  bucket = s3.Bucket( AWS_S3_BUCKET )

  def upload_file(self, file):
    try:
        
        # upload raw file
        self.bucket.put_object(Key= self.AWS_S3_FOLDER + self.FILE_NAME, Body=file)
        
        # download qr bargode image
        key = self.AWS_S3_FOLDER + self.FILE_NAME.replace('.raw','-qr.png')
        while True:
            try:
              self.bucket.download_file( key, 'code.png' )
              break
            except:
              time.sleep(0.4)
        
        # print qr barcode screen
        Draw.qr_barcode()

        ## wait 10 second on qr barcode screen
        time.sleep(10)

        # draw main screen
        Draw.logo()

    except ClientError as e:
        print(e)