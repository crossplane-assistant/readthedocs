
from diagrams import Cluster, Diagram
from diagrams.k8s.compute import Pod, Deployment
from diagrams.k8s.network import Service, Ingress

graph_attr = {
    "fontsize": "30",
    "bgcolor": "transparent",
    "size": "30",
    "margin": "-2"
}

with Diagram("Kubernetes Architecture", show=False, filename="kubernetes-architecture", graph_attr=graph_attr):
    cluster_attr = {
        "fontsize": "20",
        "margin": "20"
    }
    with Cluster("Kubernetes Cluster", graph_attr=cluster_attr):
        app_attr = {
            "fontsize": "15",
            "margin": "15"
        }
        with Cluster("Crossplane Assistant", graph_attr=app_attr):
            ca_ui_ing = Ingress("UI")
            ca_ui_svc = Service("UI")
            ca_ui_dep = Deployment("UI")
            ca_ui_pod = Pod("UI")
            ca_ui_ing >> ca_ui_svc
            ca_ui_dep - ca_ui_pod
            ca_ui_svc >> ca_ui_pod

            ca_api_svc = Service("API")
            ca_api_dep = Deployment("API")
            ca_api_pod = Pod("API")
            ca_api_dep - ca_api_pod
            ca_api_svc >> ca_api_pod

            ca_ui_pod >> ca_api_svc

        with Cluster("Kubernetes API Server", graph_attr=app_attr):
            k8s_api_svc = Service("API Server")
            k8s_api_dep = Deployment("API Server")
            k8s_api_pod = Pod("API Server")
            k8s_api_dep - k8s_api_svc
            k8s_api_svc >> k8s_api_pod
        
        ca_api_pod >> k8s_api_svc
        
