# UC01 - Select an Athlete to Train

## Related Requirements

- FR01: The application can be used by multiple athletes.

## Goal in Context

The User select the Athlete whose data will be used from that point on.

## Preconditions

The application is started and the list of Athletes is retrieved from the database.

## Successfull End Condition

The selected Athlete's data are loaded in the application.

## Failed End Condition

The Athlete's data cannot be loaded: either they don't exists in the database or there is a problem with the database.

## Primary Actors

Athlete

## Secondary Actors

None

## Trigger

The Athlete wants to load its own schedule.

## Included Cases

None

## Main Flow

1. The `Athlete` start the application.
2. The list of all existing athletes is retrieved from the database.
3. The `Athlete` select their own record from the list.
4. The application load the athlete's training data from the database.
5. The `Athlete` can start their training.

## Extensions

2.1 The list of athletes cannot be retrieved from the database.
4.1 The athlete's training data cannot be retrieved from the database.
