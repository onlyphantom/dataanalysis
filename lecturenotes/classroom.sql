CREATE TABLE [Cohort] ( 
	[CohortId] INTEGER  NOT NULL PRIMARY KEY, 
	[CohortName] NVARCHAR(50)  NOT NULL  
); 
CREATE TABLE [Students] (  
	[StudentId] INTEGER  PRIMARY KEY NOT NULL,
	[StudentName] NVARCHAR(50) NOT NULL, 
	[CohortId] INTEGER  NULL,   
	[Company] DATE  NULL  
);     
CREATE TABLE [Specialization] (  
	[SpecializationId] INTEGER  NOT NULL PRIMARY KEY,  
	[Specializationname] NVARCHAR(50)  NOT NULL  
); 
CREATE TABLE [Score] (  
	[StudentId] INTEGER  NOT NULL,  
	[SpecializationId] INTEGER  NOT NULL,  
	[Score] INTEGER  NULL  
); 