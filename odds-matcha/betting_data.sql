-- WARNING: This schema is for context only and is not meant to be run.
-- Table order and constraints may not be valid for execution.

CREATE TABLE betting_data.alert_channels (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  alert_id uuid NOT NULL,
  discord_channel text NOT NULL,
  discord_message_id text NOT NULL,
  created_at timestamp without time zone DEFAULT now(),
  CONSTRAINT alert_channels_pkey PRIMARY KEY (id),
  CONSTRAINT alert_channels_alert_id_fkey FOREIGN KEY (alert_id) REFERENCES betting_data.alerts(id)
);
CREATE TABLE betting_data.alert_thresholds (
  table_name text NOT NULL,
  min_rating numeric NOT NULL,
  team_news boolean,
  CONSTRAINT alert_thresholds_pkey PRIMARY KEY (table_name)
);
CREATE TABLE betting_data.alerts (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  event text NOT NULL,
  market text NOT NULL,
  participant text NOT NULL,
  back_bookie text NOT NULL,
  back_odds numeric NOT NULL,
  lay_bookie text NOT NULL,
  lay_odds numeric NOT NULL,
  rating numeric NOT NULL,
  created_at timestamp without time zone DEFAULT now(),
  extra_data jsonb,
  CONSTRAINT alerts_pkey PRIMARY KEY (id)
);
CREATE TABLE betting_data.bookmaker_aliases (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  alias_name text NOT NULL,
  primary_bookmaker_id uuid,
  CONSTRAINT bookmaker_aliases_pkey PRIMARY KEY (id),
  CONSTRAINT bookmaker_aliases_primary_bookmaker_id_fkey FOREIGN KEY (primary_bookmaker_id) REFERENCES betting_data.bookmakers(id)
);
CREATE TABLE betting_data.bookmaker_event_mapping (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  event_id uuid,
  bookmaker_id uuid,
  bookmaker_event_id text NOT NULL,
  CONSTRAINT bookmaker_event_mapping_pkey PRIMARY KEY (id),
  CONSTRAINT bookmaker_event_mapping_bookmaker_id_fkey FOREIGN KEY (bookmaker_id) REFERENCES betting_data.bookmakers(id),
  CONSTRAINT bookmaker_event_mapping_event_id_fkey FOREIGN KEY (event_id) REFERENCES betting_data.events(id)
);
CREATE TABLE betting_data.bookmaker_market_mapping (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  market_id uuid,
  bookmaker_id uuid,
  bookmaker_market_id text NOT NULL,
  CONSTRAINT bookmaker_market_mapping_pkey PRIMARY KEY (id),
  CONSTRAINT bookmaker_market_mapping_market_id_fkey FOREIGN KEY (market_id) REFERENCES betting_data.markets(id),
  CONSTRAINT bookmaker_market_mapping_bookmaker_id_fkey FOREIGN KEY (bookmaker_id) REFERENCES betting_data.bookmakers(id)
);
CREATE TABLE betting_data.bookmaker_participant_mapping (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  participant_id uuid,
  bookmaker_id uuid,
  bookmaker_participant_id text NOT NULL,
  CONSTRAINT bookmaker_participant_mapping_pkey PRIMARY KEY (id),
  CONSTRAINT bookmaker_participant_mapping_participant_id_fkey FOREIGN KEY (participant_id) REFERENCES betting_data.participants(id),
  CONSTRAINT bookmaker_participant_mapping_bookmaker_id_fkey FOREIGN KEY (bookmaker_id) REFERENCES betting_data.bookmakers(id)
);
CREATE TABLE betting_data.bookmakers (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  name text NOT NULL,
  default_back_lay text NOT NULL DEFAULT 'back'::text CHECK (default_back_lay = ANY (ARRAY['back'::text, 'lay'::text])),
  CONSTRAINT bookmakers_pkey PRIMARY KEY (id)
);
CREATE TABLE betting_data.event_tags (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  event_id uuid,
  tag_id uuid,
  CONSTRAINT event_tags_pkey PRIMARY KEY (id),
  CONSTRAINT event_tags_event_id_fkey FOREIGN KEY (event_id) REFERENCES betting_data.events(id),
  CONSTRAINT event_tags_tag_id_fkey FOREIGN KEY (tag_id) REFERENCES betting_data.tags(id)
);
CREATE TABLE betting_data.event_types (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  type_name text NOT NULL,
  CONSTRAINT event_types_pkey PRIMARY KEY (id)
);
CREATE TABLE betting_data.events (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  name text NOT NULL,
  event_date timestamp without time zone NOT NULL,
  event_type_id uuid,
  CONSTRAINT events_pkey PRIMARY KEY (id),
  CONSTRAINT events_event_type_id_fkey FOREIGN KEY (event_type_id) REFERENCES betting_data.event_types(id)
);
CREATE TABLE betting_data.markets (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  event_id uuid,
  market_name text NOT NULL,
  CONSTRAINT markets_pkey PRIMARY KEY (id),
  CONSTRAINT markets_event_id_fkey FOREIGN KEY (event_id) REFERENCES betting_data.events(id)
);
CREATE TABLE betting_data.odds (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  participant_id uuid,
  event_id uuid,
  market_id uuid,
  bookmaker_id uuid,
  odds numeric NOT NULL,
  back_lay text CHECK (back_lay = ANY (ARRAY['back'::text, 'lay'::text])),
  last_updated timestamp without time zone DEFAULT now(),
  CONSTRAINT odds_pkey PRIMARY KEY (id),
  CONSTRAINT odds_market_id_fkey FOREIGN KEY (market_id) REFERENCES betting_data.markets(id),
  CONSTRAINT odds_participant_id_fkey FOREIGN KEY (participant_id) REFERENCES betting_data.participants(id),
  CONSTRAINT odds_bookmaker_id_fkey FOREIGN KEY (bookmaker_id) REFERENCES betting_data.bookmakers(id),
  CONSTRAINT odds_event_id_fkey FOREIGN KEY (event_id) REFERENCES betting_data.events(id)
);
CREATE TABLE betting_data.participants (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  participant_name text NOT NULL,
  status boolean DEFAULT true,
  market_id uuid,
  CONSTRAINT participants_pkey PRIMARY KEY (id),
  CONSTRAINT participants_market_id_fkey FOREIGN KEY (market_id) REFERENCES betting_data.markets(id)
);
CREATE TABLE betting_data.racing (
  event_id uuid,
  event_name text,
  event_date timestamp without time zone,
  market_id uuid,
  market_name text,
  participant_id uuid,
  participant_name text,
  back_bookmaker text,
  back_odds numeric,
  lay_bookmaker text,
  lay_odds numeric,
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  CONSTRAINT racing_pkey PRIMARY KEY (id),
  CONSTRAINT racing_event_id_fkey FOREIGN KEY (event_id) REFERENCES betting_data.events(id)
);
CREATE TABLE betting_data.racing_staging (
  event_id uuid,
  event_name text,
  event_date timestamp without time zone,
  market_id uuid,
  market_name text,
  participant_id uuid,
  participant_name text,
  back_bookmaker text,
  back_odds numeric,
  lay_bookmaker text,
  lay_odds numeric,
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  CONSTRAINT racing_staging_pkey PRIMARY KEY (id),
  CONSTRAINT racing_staging_event_id_fkey FOREIGN KEY (event_id) REFERENCES betting_data.events(id)
);
CREATE TABLE betting_data.tags (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  tag_name text NOT NULL UNIQUE,
  CONSTRAINT tags_pkey PRIMARY KEY (id)
);
CREATE TABLE betting_data.trigger_log (
  id integer NOT NULL DEFAULT nextval('betting_data.trigger_log_id_seq'::regclass),
  event text,
  calculated_rating numeric,
  threshold numeric,
  action text,
  created_at timestamp without time zone DEFAULT now(),
  CONSTRAINT trigger_log_pkey PRIMARY KEY (id)
);
CREATE TABLE betting_data.two_up (
  event_id uuid,
  event_name text,
  event_date timestamp without time zone,
  market_id uuid,
  market_name text,
  participant_id uuid,
  participant_name text,
  back_bookmaker text,
  back_odds numeric,
  lay_bookmaker text,
  lay_odds numeric,
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  CONSTRAINT two_up_pkey PRIMARY KEY (id),
  CONSTRAINT two_up_event_id_fkey FOREIGN KEY (event_id) REFERENCES betting_data.events(id)
);
CREATE TABLE betting_data.two_up_staging (
  event_id uuid,
  event_name text,
  event_date timestamp without time zone,
  market_id uuid,
  market_name text,
  participant_id uuid,
  participant_name text,
  back_bookmaker text,
  back_odds numeric,
  lay_bookmaker text,
  lay_odds numeric,
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  CONSTRAINT two_up_staging_pkey PRIMARY KEY (id)
);