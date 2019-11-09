from unittest.mock import Mock, patch
from boto.ec2.connection import EC2Connection
import boto
from moto import mock_ec2_deprecated, mock_ec2
from AWS.resources.aws import awsConnectRegion, AWSlistInstance

class Test_awsConnectRegion:

    def test_awsconnectresion_instatiation(self):
        awsins = awsConnectRegion(aws_id='xxx', aws_secret='asd12323')
        assert isinstance(awsins, awsConnectRegion)

    @mock_ec2_deprecated
    def test_connect_to_region(self):
        awsins = awsConnectRegion(aws_id='xxx', aws_secret='asd12323')
        result = awsins.connect_to_region('us-east-1')
        assert isinstance(result, EC2Connection)



class TestAWSlistInstance:

    @mock_ec2_deprecated
    @mock_ec2
    @patch.object(AWSlistInstance, 'listAllInstance')
    def test_listAllInstance(self, mock_instances):
        mock_instances.return_value = ['Instance:i-03117ab1abf9992e9', 'Instance:i-0c6aef3dfd797d6ac']
        aswlistins = AWSlistInstance(aws_id='xxx', aws_secret='yyy123')
        result = aswlistins.listAllInstance('us-east-1')
        assert result == ['Instance:i-03117ab1abf9992e9','Instance:i-0c6aef3dfd797d6ac']








