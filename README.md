This repo contains the code used for the Infrastructure as Code talk done on [Jan 07th 2022 (French)](https://youtu.be/lIAGO5RKdJQ) 

I talk about Terraform, Ansible and Pulumi and deploy S3 buckets, EC2 instances, static websites, EKS cluster...

The slides are available [here](Infrastructure_As_Code.pdf)

#### Terraform

To use this Terraform code, you need to install Terraform CLI, clone this repo, then use the following commands:

```
terraform init
terraform plan
terraform apply
terraform destroy (to take down all your stuff)
```

#### Pulumi

To use this Terraform code , you need to install for homebrew, or cholatery, or..., clone this repo, then use the following commands:
(a virtual environnement should be automatically created, and requirements.txt packages should be installed)

```
pulumi new
pulumi up
pulumi destroy (to take down all your stuff)
```

##### Documentations

[Terraform](https://www.terraform.io/docs)
[Ansible](https://docs.ansible.com/ansible/latest/)
[Pulumi](https://pulumi.com/docs/)

