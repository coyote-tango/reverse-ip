variable "region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-2"
}

variable "prefix" {
  description = "Prefix to add to AWS resources"
  type        = string
  default     = "reverse-ip"

}
