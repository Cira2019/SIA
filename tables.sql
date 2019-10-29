

CREATE TABLE interventions(
	id serial PRIMARY KEY,
	intervention_name VARCHAR(50),
	intervention_code VARCHAR(15)
);


INSERT INTO interventions (intervention_name) VALUES('Measles');
INSERT INTO interventions (intervention_name) VALUES('MR');
INSERT INTO interventions (intervention_name) VALUES('OPV');
INSERT INTO interventions (intervention_name) VALUES('IPV');
INSERT INTO interventions (intervention_name) VALUES('Vitamin A');
INSERT INTO interventions (intervention_name) VALUES('Bednet');
INSERT INTO interventions (intervention_name) VALUES('Albendazole');
INSERT INTO interventions (intervention_name) VALUES('Mebendazole');
INSERT INTO interventions (intervention_name) VALUES('Yellow fever');
INSERT INTO interventions (intervention_name) VALUES('Japanese encephalitis');