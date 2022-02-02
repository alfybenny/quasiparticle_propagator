# quasiparticle_propagator

Working classes:

<ul>
    <li>input_processing: Contains <b>xyz</b>, <b>mol2</b> and <b>pdb</b> classes.</li>
    <ul>Modules added so far:
        <li>system_name.indexify() - convert the bare numpy array of atomic coordinates into lists of list, where each inside list contains coordinate of a molecule and store it as 'crystal'</li>
        <li>system_name.mol_coor(index) - reutrns a numpy array of molecular coordinates for that particular index.</li>
        <li></li>
    </ul>
</ul>


<ul>
    <li>mon_prop.Property: Contains <b>trans_dipole</b>, <b>trans_charge</b>, <b>trans_dens</b> and <b>mol_orb</b></li>
    <ul>Modules added so far:
        <li>operator_name.coor_to_cent(array, no_of_atoms)</li>
    </ul>
</ul>