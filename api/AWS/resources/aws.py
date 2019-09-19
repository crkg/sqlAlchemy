import boto3
import sys
import boto
import boto.ec2
import boto.utils

# auth = {"aws_access_key_id": "AKIAIR36LFO6363OXEQQ",
#        "aws_secret_access_key": "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"}


def exception_handling(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e1:
            error1 = "Error1: {}".format(e1)
            print(error1)
            sys.exit(0)
    return inner


class awsConnectRegion(object):
    def __init__(self, aws_id="AKIAIF35ZV3HKMYC2HUQ", aws_secret="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"):
        self.auth = dict()
        self.auth['aws_access_key_id'] = aws_id
        self.auth['aws_secret_access_key'] = aws_secret

    @exception_handling
    def connect_to_region(self, region_name):
        # change "eu-west-1" region if different
        ec2 = boto.ec2.connect_to_region(region_name, **self.auth)
        return ec2


class AWSlistInstance(awsConnectRegion):

    def __init__(self, aws_id="AKIAIF35ZV3HKMYC2HUQ", aws_secret="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"):
        super().__init__(aws_id=aws_id, aws_secret=aws_secret)

    @exception_handling
    def listAllInstance(self, region_name):
        print("Listing all instance in region {} ".format(region_name))
        ec2 = self.connect_to_region(region_name)
        reservations = ec2.get_all_instances()
        return [i.instances for i in reservations]

    @exception_handling
    def listAInstance(self,region_name,instance_id):
        awsList = self.listAllInstance(region_name)
        print(f"aws instances \n {awsList}")
        for each in awsList:
            if instance_id == each[0].id:
                return each[0].state
        return None



class AWSlistS3bucket(awsConnectRegion):
    @exception_handling
    def s3bucket(self, region_name, instnc):
        print("List all existing buckets for the AWS account")
        ec2 = self.connect_to_region(region_name)
        ec2.list_buckets()


class AwsOperation(awsConnectRegion):

    @exception_handling
    def startInstance(self, region_name, instnc):
        print("Starting the instance...")
        ec2 = self.connect_to_region(region_name)
        ec2.start_instances(instance_ids=instnc)

    @exception_handling
    def stopInstance(self, region_name, instnc):
        print("Stopping the instance...")
        ec2 = self.connect_to_region(region_name)
        ec2.stop_instances(instance_ids=instnc)

    @exception_handling
    def terminate(self, region_name, instnc):
        print("Terminating an instance...")
        ec2 = self.connect_to_region(region_name)
        ec2.terminate_instances(instance_ids=instnc)

    @exception_handling
    def s3bucket(self, region_name, instnc):
        print("List all existing buckets for the AWS account")
        ec2 = self.connect_to_region(region_name)
        ec2.list_buckets()


def main():
    # read arguments from the command line and
    # check whether at least two elements were entered
    if len(sys.argv) < 3:
        print("Usage arguments are space seperated: python aws.py {start|stop|terminate|awsRegion}\n")
        sys.exit(0)
    else:
        action = sys.argv[1]
        awsRegion = sys.argv[2]
        # awsAccessKey = sys.argv[3]
        # awsSecretKey = sys.argv[4]
        Instance = AWSlistInstance()
        list = Instance.listAllInstance(awsRegion)

        print("Here is the list of instance on region {}, {}".format(awsRegion, list))
        for i in list:
            instnc = i[0].id
            awsop = AwsOperation()
            if action == "start":
                awsop.startInstance(awsRegion, instnc)
            elif action == "stop":
                awsop.stopInstance(awsRegion, instnc)
            elif action == "terminate":
                awsop.terminate(awsRegion, instnc)
            else:
                print("Usage arguments are space seperated: python aws.py {start|stop|terminate|awsRegion}\n")


if __name__ == '__main__':
    main()
