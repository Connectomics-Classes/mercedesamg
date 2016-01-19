warning('off','all');
%get_template;
zStart = 1025;
zStop = 1050;
zSlice = [zStart, zStop];
padX = 50; padY = 50; padZ = 2;

%[eData, mData, sData, vData] = get_ac3_data(zSlice(1),zSlice(2), padX, padY, padZ);
%% Load Data
oo = OCP();
oo.setImageToken('kasthuri11cc');
oo.setImageChannel('image');

oo.setAnnoToken('kat11vesicles');
oo.setAnnoChannel('annotation');

q = OCPQuery;
q.setType(eOCPQueryType.imageDense);
q.setCutoutArgs([2776, 4776],[7000,9000],[1004,1154],1);
q.setCutoutArgs([4776, 5776],[8500,9500],[1150,1200],1);
q.validate;

eData = oo.query(q);

q.setType(eOCPQueryType.annoDense);
vData = oo.query(q);
image(vData)



%% Manipulate Data
cube = eData.clone;
save('eData.mat','cube');

vesicledetect_quick('eData.mat','vesicle_templates_kasthuri11cc.mat',1,3,120,1.25,0,padX,padY,padZ,'results.mat');

load('results.mat');
results = cube;
h = image(eData);h.associate(results);
cropVolume('eData.mat','eData.mat',padX,padY,padZ);

cube = vData.clone;
save('vData.mat','cube');
cropVolume('vData.mat','vData.mat',padX,padY,padZ);

cube = 0;
load('results.mat');
results = cube;

load('eData.mat');
eData = cube;

cube=0;
load('vData.mat');
vData = cube;

h=image(vData);h.associate(results);
pr_objects('results.mat','vData.mat','metrics.mat');

warning('on','all');
