# Compositions

## List View

The List view shows the claims in a table. The table shows the attributes:

* Composition name
* Kubernetes Kind
* Age

The table is paginated and you can filter the compositions by the composition name.

![Panel Compositions - List](./view-compositions_list.png)

## Composition View

### View Tab

The Details view allow you to see the composition in a graph view. The graph is composed of objects, events and templates. The graph is interactive, you can click on the objects to see more details.

![Panel Compositions - Details](./view-compositions_panel-details_tab-event.png)

#### Detail Subtab

![Panel Compositions - Details - Tab Manifest - Sub-tab Detail](./view-compositions_panel-details_tab-manifest_subtab-detail.png)

The Subtab Detail sumup the information of the object in the Composition.

#### Kubernetes Subtab

![Panel Compositions - Details - Tab Manifest - Sub-tab Kubernetes](./view-compositions_panel-details_tab-manifest_subtab-kubernetes.png)

The Subtab Kubernetes shows the Kubernetes YAML of the generated object.

#### YAML Subtab

![Panel Compositions - Details - Tab Manifest - Sub-tab YAML](./view-compositions_panel-details_tab-manifest_subtab-yaml.png)

The Subtab YAML shows the YAML of the object in the Composition.

#### Dependencies Subtab

##### Graph

![Panel Compositions - Details - Tab Manifest - Sub-tab Dependencies](./view-compositions_panel-details_tab-manifest_subtab-dependencies.png)

The Subtab Dependencies shows the dependencies of the object in the Composition in a graph view.

##### Object interaction

![Panel Compositions - Details - Tab Manifest - Sub-tab Dependencies - Focus object](./view-compositions_panel-details_tab-manifest_subtab-dependencies_focus-object-1.png)

The Subtab Dependencies shows the related code of the object in the Composition and the way it is composed across the objects.

### Manifest Tab

The view of the objects in the graph is divided in three tabs: Manifest, Event and Template.

![Panel Compositions - Details - Tab Manifest](./view-compositions_panel-details_tab-manifest.png)
