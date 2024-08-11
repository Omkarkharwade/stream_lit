import streamlit as st

# App Title
st.title("Warehouse Inventory Management System")

# Sidebar for Navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ['Dashboard', 'Transport Vehicles', 'Warehouse Equipment', 'Packaging Materials',
                                      'Tracking & Management Software', 'Logistics Services', 'Cargo Handling Equipment', 
                                      'Supply Chain Solutions'])

# Dashboard
if options == 'Dashboard':
    st.header("Dashboard")
    st.write("This is the dashboard with key metrics and insights.")
    # Add graphs, metrics, etc.

# Transport Vehicles Management
elif options == 'Transport Vehicles':
    st.header("Manage Transport Vehicles")
    
    with st.form(key='vehicle_form'):
        vehicle_type = st.selectbox("Vehicle Type", ["Truck", "Ship", "Airplane", "Train"])
        vehicle_id = st.text_input("Vehicle ID")
        vehicle_capacity = st.number_input("Capacity (tons)", min_value=0.0, step=0.1)
        vehicle_status = st.selectbox("Status", ["Available", "In Transit", "Under Maintenance"])
        submit_vehicle = st.form_submit_button(label='Submit')

    if submit_vehicle:
        st.write(f"Vehicle Type: {vehicle_type}")
        st.write(f"Vehicle ID: {vehicle_id}")
        st.write(f"Vehicle Capacity: {vehicle_capacity} tons")
        st.write(f"Vehicle Status: {vehicle_status}")
        st.success("Vehicle data submitted successfully!")

# Warehouse Equipment Management
elif options == 'Warehouse Equipment':
    st.header("Manage Warehouse Equipment")
    
    with st.form(key='equipment_form'):
        equipment_type = st.selectbox("Equipment Type", ["Forklift", "Pallet Jack", "Shelving Unit", "Storage System"])
        equipment_id = st.text_input("Equipment ID")
        equipment_status = st.selectbox("Status", ["Operational", "Under Maintenance", "Out of Service"])
        submit_equipment = st.form_submit_button(label='Submit')

    if submit_equipment:
        st.write(f"Equipment Type: {equipment_type}")
        st.write(f"Equipment ID: {equipment_id}")
        st.write(f"Equipment Status: {equipment_status}")
        st.success("Equipment data submitted successfully!")

# Packaging Materials Management
elif options == 'Packaging Materials':
    st.header("Manage Packaging Materials")
    
    with st.form(key='packaging_form'):
        material_type = st.selectbox("Material Type", ["Box", "Pallet", "Crate", "Protective Material"])
        material_quantity = st.number_input("Quantity", min_value=0)
        submit_material = st.form_submit_button(label='Submit')

    if submit_material:
        st.write(f"Material Type: {material_type}")
        st.write(f"Quantity: {material_quantity}")
        st.success("Packaging material data submitted successfully!")

# Tracking and Management Software
elif options == 'Tracking & Management Software':
    st.header("Tracking and Management Software")
    
    with st.form(key='software_form'):
        software_type = st.selectbox("Software Type", ["Shipment Tracking", "Inventory Management", "Supply Chain Optimization"])
        software_version = st.text_input("Software Version")
        submit_software = st.form_submit_button(label='Submit')

    if submit_software:
        st.write(f"Software Type: {software_type}")
        st.write(f"Software Version: {software_version}")
        st.success("Software data submitted successfully!")

# Logistics Services Management
elif options == 'Logistics Services':
    st.header("Manage Logistics Services")
    
    with st.form(key='logistics_form'):
        service_type = st.selectbox("Service Type", ["Third-party Logistics (3PL)", "Freight Forwarding", "Courier and Delivery"])
        service_provider = st.text_input("Service Provider")
        submit_service = st.form_submit_button(label='Submit')

    if submit_service:
        st.write(f"Service Type: {service_type}")
        st.write(f"Service Provider: {service_provider}")
        st.success("Logistics service data submitted successfully!")

# Cargo Handling Equipment Management
elif options == 'Cargo Handling Equipment':
    st.header("Cargo Handling Equipment")
    
    with st.form(key='cargo_form'):
        equipment_type = st.selectbox("Equipment Type", ["Crane", "Conveyor", "Loading/Unloading Dock"])
        equipment_status = st.selectbox("Status", ["Operational", "Under Maintenance", "Out of Service"])
        submit_cargo = st.form_submit_button(label='Submit')

    if submit_cargo:
        st.write(f"Equipment Type: {equipment_type}")
        st.write(f"Equipment Status: {equipment_status}")
        st.success("Cargo handling equipment data submitted successfully!")

# Supply Chain Solutions Management
elif options == 'Supply Chain Solutions':
    st.header("Supply Chain Solutions")
    
    with st.form(key='supply_chain_form'):
        solution_type = st.selectbox("Solution Type", ["Procurement Software", "Order Management System", "Transportation Management System (TMS)"])
        solution_provider = st.text_input("Solution Provider")
        submit_solution = st.form_submit_button(label='Submit')

    if submit_solution:
        st.write(f"Solution Type: {solution_type}")
        st.write(f"Solution Provider: {solution_provider}")
        st.success("Supply chain solution data submitted successfully!")








