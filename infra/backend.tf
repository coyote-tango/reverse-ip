terraform {
  backend "s3" {
    bucket         = "playground-buckety"
    key            = "terraform/"
    region         = "us-east-2"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
  }
}
