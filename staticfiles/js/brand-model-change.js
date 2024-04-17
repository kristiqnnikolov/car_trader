document.addEventListener('DOMContentLoaded', function () {
    var brandRadios = document.querySelectorAll('input[name="brand"]');

    brandRadios.forEach(function (radio) {
        radio.addEventListener('change', function () {
            var selectedBrand = this.value;
            var models = getModelOptions(selectedBrand);
            updateModelOptions(models);
        });
    });
    function getModelOptions(brand) {
        var modelMap = {
            'Acura': ['Integra', 'TLX', 'MDX', 'RDX', 'ZDX', 'NSX', 'RL', 'TL', 'RSX', 'TSX', 'CSX',],
            'Alfa Romeo': ['145', '146', '147', '155', '156', '159', '164', 'Brera', 'Crosswagon Q4',
                'Giulia', 'GT', 'GTV', 'MiTo', 'Tonale', 'Spider'],
            'Aston Martin': ['DBS', 'DBX', 'DB7', 'DB9', 'Rapide', 'Vantage V12', 'Vantage V8', 'Vanquish'],
            "Audi": ['50', '60', '80', '90', '100', '200', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
                'Allroad', 'Coupe', 'E-Tron', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Quattro', 'R8', 'RSQ3',
                'RSQ8', 'RS3', 'RS4', 'RS5', 'RS6', 'RS7', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'SQ5',
                'SQ7', 'Spider', 'TT'],
            "BMW": ['1 серия', '2 серия', '3 серия', '4 серия', '5 серия', '6 серия', '7 серия', '8 серия', 'M серия',
                'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'XM', 'Z1', 'Z2', 'Z3', 'Z8', 'i3', 'i4', 'i7', 'i8', 'iX', 'iX3'],
            "Bentley": ['Arnage', 'Azure', 'Bentayga', 'Continental', 'Flying Spur'],
            "Cadillac": ['ATS', 'CTS', 'DTS', 'Deville', 'Eldorado', 'Escalade', 'Fleetwood', 'STS', 'Seville', 'SRX',
                'XT4'],
            "Chevrolet": ['Alero', 'Astro', 'Avalanche', 'Aveo', 'Beretta', 'Blazer', 'Bolt', 'Camaro', 'Cobalt',
                'Corvette', 'Cruze', 'Epica', 'HHR', 'Kalos', 'Lacetti', 'Malibu', 'Matiz', 'Nubira', 'Orlando', 'Spark',
                'Suburban', 'Tacuma', 'Tahoe', 'Trailblazer', 'Trax', 'Volt'],
            "Chrysler": ['200', '300c', '300m', 'Crossfire', 'Gr. Voyager', 'Pacifica', 'Pt Cruiser', 'Sebring',
                'Stratus', 'Town and Country'],
            "Citroen": ['Berlingo', 'C-Zero', 'C-Crosser', 'C-Elysee', 'C1', 'C2', 'C3', 'C4', 'C4 Picasso',
                'C5', 'C6', 'C8', 'DS 4 Crossback', 'DS 7 Crossback', 'DS3', 'DS4', 'DS5', 'Evasion', 'Grand C4 Picasso',
                'Jumpy', 'Nemo', 'Saxo', 'Spacetourer', 'Xantia', 'Xsara', 'Xsara Picasso', 'Zx'],
            "DS": ['3', '3 Crossback', '4', '4 Crossback', '5', '7', '7 Crossback', '9'],
            "Dacia": ['Dokker', 'Duster', 'Jogger', 'Lodgy', 'Logan', 'Sandero', 'Spring'],
            "Daewoo": ['Evanda', 'Kalos', 'Lacetti', 'Lanos', 'Matiz', 'Nexia', 'Nubira', 'Tacuma'],
            "Dodge": ['Avenger', 'Caliber', 'Caravan', 'Challenger', 'Charger', 'Dart', 'Durango', 'Journey',
                'Neon', 'Nitro', 'RAM 1500', 'RAM 2500', 'RAM', 'Viper'],
            "Genesis": ['G70', 'G80', 'G90', 'GV60', 'GV70', 'GV80'],
            "Great Wall": ['Hover Cuv', 'Hover H5', 'Hover H6', 'Poer', 'Safe', 'Steed 3', 'Steed 5',
                'Steed 6', 'Steed 7', 'Voleex C10', 'Voleex C20', 'Voleex C30'],
            "Haval": ['Dargo', 'F7x', 'H2', 'H6', 'Jolion'],
            "Honda": ['Accord', 'Civic', 'Cr-v', 'Cr-x', 'Crz', 'Fr-v', 'Hr-v', 'Insight', 'Jazz', 'Legend',
                'Odyssey', 'Pilot', 'Prelude', 'Ridgeline', 'S2000', 'Stream'],
            "Hummer": ['H1', 'H2', 'H3'],
            "Hyundai": ['Accent', 'Atos', 'Bayon', 'Coupe', 'Elantra', 'Galloper', 'Genesis', 'Getz', 'Grandeur',
                'I10', 'I20', 'I30', 'I40', 'IX35', 'IX55', 'Ioniq', 'Ioniq 5', 'Ioniq 6', 'Ix20', 'Kona', 'Matrix',
                'Palisade', 'Santa Fe', 'Sonata', 'Starex', 'Staria', 'Terracan', 'Trajet', 'Tucson', 'Veloster', 'Xg'],
            "Infiniti": ['Ex30', 'Ex35', 'Ex37', 'Fx30', 'Fx35', 'Fx37', 'Fx45', 'Fx50', 'G', 'J', 'M', 'Q', 'Q30',
                'Q40', 'Q50', 'QX30', 'QX50', 'QX56', 'QX60', 'QX70', 'QX80'],
            "Isuzu": ['D-Max', 'Trooper'],
            "Jaguar": ['E-Pace', 'F-Pace', 'F-Type', 'I-Pace', 'S-Type', 'X-Type', 'XE', 'XF', 'XJ', 'XKR'],
            "Jeep": ['Cherokee', 'Commander', 'Compass', 'Grand Wagoneer', 'Grand Cherokee', 'Patrior', 'Wrangler', 'Renegade'],
            "Kia": ['Carens', 'Carnival', 'Ceed', 'Cerato', 'EV6', 'Forte', 'K5', 'K7', 'K9', 'Magentis', 'Niro',
                'Opirus', 'Optima', 'Picanto', 'Pro Ceed', 'Rio', 'Sedona', 'Seltos', 'Sorento', 'Soul', 'Sportage',
                'Stinger', 'Stonic', 'Telluride', 'Venga', 'X Ceed'],
            "Lada": ['1200', '1300', '1500', '1600', '2100', '21011', '21013', '2102', '2103', '2104', '21043',
                '2105', '21061', '2107', '2110', 'Granta', 'Kalina', 'Niva', 'Vesta'],
            "Lamborghini": ["Aventador", "Countach", "Diablo", "Gallardo", "Huracan", "Murcielago", "Reventon", "Urus", "Veneno"],
            "Lancia": ["Delta", "Kappa", "Lybra", "Musa", "Phedra", "Thema", "Thesis", "Voyager", "Y", "Ypsilon"],
            "Land Rover": ["Defender", "Discovery", "Evoque", "Freelander", "Range Rover Evoque", "Range Rover Sport", "Range Rover Velar", "Range Rover"],
            "Lexus": ["CT200h", "ES", "GX 460", "GX 470", "GS", "IS", "LC", "LS", "LX", "NX", "RC", "RX", "RX200T", "RX300", "RX330", "RX350", "RX400H", "RX450", "UX"],
            "Lincoln": ["MKX", "MKZ", "Navigator", "Town Car"],
            "Maserati": ["Ghibli", "GranTurismo", "Grecale", "Levante", "MC20", "Quattroporte"],
            "Maybach": ["57", "62", "S 560", "S 580"],
            "Mazda": ["2", "3", "5", "6", "323", "626", "B2500", "BT-50", "CX-3", "CX-5", "CX-7", "CX-9", "CX-30", "CX-60", "MX-30", "MPV", "MX-3", "MX-5", "MX-6", "Premacy", "RX-7", "RX-8", "Tribute", "Xedos"],
            "McLaren": ["540C Coupe", "560C Coupe", "650 S", "720 S", "GT", "MP4-12C"],
            "Mercedes-Benz": ["110", "111", "113", "114", "115", "116", "123", "124", "126", "126-260",
                "170", "180", "190", "200", "220", "230", "240", "250", "260", "280", "300", "320", "350", "420",
                "450", "500", "560", "A", "B", "C", "CL", "CLA", "CLC", "CLS", "Citan", "E", "EQA", "EQB", "EQC", "EQE", "EQS", "EQV",
                "G", "GL", "GLA", "GLB", "GLC", "GLE", "GLK", "GLS", "GT 4-Door Coupe", "M", , "MB",
                "ML", "R", "S ", "SL ", "SLC", "SLK", "SLR", "SLS", "SPRINTER", "V", "Vaneo", "Viano", "Vito", "X", "Z ",],
            "MG": ["3", "5", "6", "7", "Astro", "B", "Express", "F", "GT", "HS", "MGA", "MGB", "MGF", "Midget",
                "RV8", "SV", "TF", "ZS", "ZR", "ZS 180", "ZS EV", "ZS SUV", "ZS-T", "ZT", "ZT-T"],
            'Mitsubishi': ['3000 GT', 'ASX', 'Carisma', 'Colt', 'Eclipse', 'Eclipse Cross', 'Galant', 'Grandis',
                'I-MiEV', 'L200', 'Lancer', 'Outlander', 'Pajero', 'Space Star', 'Space Wagon'],
            'Nissan': ['200 sx', '300 zx', '350z', '370z', 'Almera', 'Almera Tino', 'Altima', 'Ariya', 'Armada',
                'Cube', 'Frontier', 'GT-R', 'Juke', 'Kubistar', 'Leaf', 'Maxima', 'Micra', 'Murano', 'Navara', 'Note',
                'Pathfinder', 'Patrol', 'Pickup', 'Pixo', 'Primera', 'Pulsar', 'Qashqai', 'Rogue', 'Sentra', 'Skyline',
                'Terrano', 'Tiida', 'Titan Crew Cab', 'Titan King', 'X-Trail', 'Xterra', 'E-NV200'],
            'Opel': ['Adam', 'Agila', 'Ampera', 'Antara', 'Astra', 'Cascada', 'Combo', 'Corsa', 'Crossland X',
                'Grandland X', 'Insignia', 'Kadett', 'Karl', 'Meriva', 'Mokka', 'Mokka X', 'Omega', 'Signum', 'Tigra',
                'Vectra', 'Zafira'],
            'Peugeot': ['106', '107', '108', '205', '206', '207', '208', '301', '306', '307', '308', '309', '405',
                '406', '407', '408', '508', '605', '607', '806', '807', '1007', '2008', '3008', '4007', '4008', '5008',
                'Bipper', 'Expert', 'Partner', 'RCZ', 'Rifter', 'Traveler', 'iOn'],
            'Porsche': ['911', '991', '996', 'Boxter', 'Carrera', 'Cayenne', 'Cayman', 'Macan', 'Panamera', 'Taycan'],
            'Renault': ['19', 'Alpine', 'Arkana', 'Austral', 'Captur', 'Clio', 'Espace', 'Express', 'Fluence',
                'Grand Escape', 'Grand Scenic', 'K-ZE', 'Kadjar', 'Kangoo', 'Koleos', 'Laguna', 'Laguna Coupe', 'Latitude',
                'Megane', 'Modus', 'Safrane', 'Scenic', 'Scenic RX4', 'Symbol', 'Talisman', 'Twingo', 'Twizy', 'Vel Satis',
                'Zoe'],
            'Rolls-royce': ['Cullinan', 'Dawn', 'Ghost', 'Phantom', 'Silver Spur', 'Wraith'],
            'Rover': ['25', '45', '75', '200', '420', '620', '825', '827', 'Streetwise'],
            'Saab': ['9-3', '9-5', '900', '9000'],
            'Seat': ['Alhambra', 'Altea', 'Arona', 'Arosa', 'Ateca', 'Cordoba', 'Exeo', 'Ibiza', 'Leon', 'Mii',
                'Tarraco', 'Toledo', 'Vario'],
            'Skoda': ['Citigo', 'Enyaq', 'Fabia', 'Felicia', 'Kamiq', 'Karoq', 'Kodiaq', 'Octavia', 'Praktik',
                'Rapid', 'Roomster', 'Scala', 'Superb', 'Yeti'],
            'Smart': ['forfour', 'fortwo', 'MC', 'Roadster'],
            'Subaru': ['Ascent', 'BRZ', 'Forester', 'G3X', 'Impreza', 'Justy', 'Legacy', 'Levorg', 'Outback',
                'Solterra', 'Trezia', 'Tribeca', 'XV'],
            'Suzuki': ['Across', 'Alto', 'Baleno', 'Celerio', 'Grand Vitara', 'Ignis', 'Jimny', 'Kizashi',
                'Liana', 'SX4', 'SX4 S-Cross', 'Samurai', 'Splash', 'Swace', 'Swift', 'Vitara', 'Wagon R', 'XL-7'],
            'Tesla': ['3', 'S', 'X', 'Y'],
            'Toyota': ['4runner', 'Auris', 'Avalon', 'Avensis', 'Avensis Verso', 'Aygo', 'C-HR', 'Camry', 'Celica',
                'Corolla', 'Corolla Cross', 'Corolla Verso', 'Fj Cruiser', 'GT86', 'Highlander', 'Hilux', 'IQ',
                'Land Cruiser', 'MR2', 'Previa', 'Prius', 'Proace City', 'Proace City Verso', 'Rav4', 'Scion',
                'Sequoia', 'Sienna', 'Supra', 'Tacoma', 'Tundra', 'Urban Cruiser', 'Venza', 'Verso', 'Verso S',
                'Yaris', 'Yaris Cross', 'Yaris Verso', 'BZ4X'],
            'VW': ['Alltrack', 'Amarok', 'Arteon', 'Atlas', 'Beetle', 'Bora', 'CC', 'Caddy', 'Corrado', 'Eos',
                'Fox', 'Golf', 'Golf Plus', 'Golf Variant', 'ID.3', 'ID.4', 'ID.5', 'ID.6', 'ID.Buzz', 'Jetta',
                'Lupo', 'Multivan', 'New Beetle', 'Passat', 'Phaeton', 'Polo', 'Scirocco', 'Sharan', 'Sportsvan',
                'T-Cross', 'T-Roc', 'Taigo', 'Tiguan', 'Touareg', 'Touran', 'Up', 'Vento'],
            'Volvo': ['C30', 'C70', 'S40', 'S60', 'S80', 'S90', 'V40', 'V40 Cross Country', 'V50', 'V60',
                'V60 Cross Country', 'V70', 'V90', 'V90 Cross Country', 'XC40', 'XC60', 'XC70', 'XC90']
        };
        return modelMap[brand] || [];
    }

    function updateModelOptions(models) {
        var modelList = document.getElementById('model-list');
        modelList.innerHTML = '';

        models.forEach(function (model) {
            var modelId = 'model_' + model.toLowerCase();
            var li = document.createElement('li');
            var input = document.createElement('input');
            input.type = 'radio';
            input.id = modelId;
            input.name = 'model';
            input.value = model;
            var label = document.createElement('label');
            label.setAttribute('for', modelId);
            label.textContent = model;
            li.appendChild(input);
            li.appendChild(label);
            modelList.appendChild(li);
        });
    }
});
