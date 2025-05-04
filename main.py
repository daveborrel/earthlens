import ee

ee.Authenticate()
ee.Initialize(project='earthlens')
print(ee.String('Hello from the Earth Engine servers!').getInfo())

# Load a Landsat image.
img = ee.Image("CPOM/CryoSat2/ANTARCTICA_DEM")

# Print image object WITHOUT call to getInfo(); prints serialized request instructions.
print(img)