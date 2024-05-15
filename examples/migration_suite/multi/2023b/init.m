a = Simulink.Signal;
a.CoderInfo.StorageClass = 'ExportedGlobal';
a.CoderInfo.Identifier   = 'a';
a.InitialValue           = '0';
a.DataType               = 'int32';

b   = copy(a);
c   = copy(a);
out = copy(a);
b.CoderInfo.Identifier     = 'b';
c.CoderInfo.Identifier     = 'c';
out.CoderInfo.Identifier   = 'out';
