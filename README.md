📌 Project 12 – Kubernetes Deployment of Python Flask App

This project demonstrates how to deploy and manage a Python Flask application on Kubernetes using Docker, kubectl, and Helm (optional). It also introduces background workloads with Kubernetes CronJobs, proving real-world DevOps and Cloud Engineering skills.

🎯 Objectives

Deploy a Python Flask app to Kubernetes as a scalable service.

Configure Kubernetes objects: Deployment, Service, ConfigMap, Secret, Ingress (optional).

Automate container build & push with Docker.

Implement a Kubernetes CronJob running a Python script.

Demonstrate monitoring, scaling, and self-healing features of Kubernetes.

Show hands-on DevOps + Python integration.
                ┌───────────────────────────────────┐
                │            Users 🌍               │
                └───────────────┬───────────────────┘
                                │
                       [Ingress / NodePort]
                                │
                        ┌───────┴────────┐
                        │  Flask Service │
                        └───────┬────────┘
                                │
                      ┌─────────┴─────────┐
                      │   Flask Pods (2)  │  <- Deployment
                      └─────────┬─────────┘
                                │
                      ┌─────────┴─────────┐
                      │ ConfigMap + Secret│
                      └────────────────────┘

                       ┌────────────────────┐
                       │  CronJob (Python)  │  -> Runs periodic batch task
                       └────────────────────┘
project12-k8s-flask-app/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│
├── screenshots/
│   ├── github-actions-build.png
│   ├── dockerhub-image.png
│   ├── kubectl-get-pods.png
│   └── browser-output.png
│
├── .github/
│   └── workflows/
│       └── docker-build-push.yml
│
└── README.md