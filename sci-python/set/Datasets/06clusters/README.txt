Geographic locations of a set of incidents.
Data from http://bombsight.org/#14/51.4465/-0.0756

File incidents.mat contains:
	- incidents = (x,y) pairs describing map coordinates, of each incident in
	  arbitrary units
	- referencepoints = xy pairs with map coordinates of four reference points
	- place1,... = names of reference points

Approximate scale is 44m per unit.

incidents.csv, incidents.npy: incident data.
reference.csv, reference.npy: reference data.
The place names are "Darrell Road", "Lyndhurst Way", "Tanner's Hill", and "Crofton Park Road"

clusters.npz: incident and reference data in single file
