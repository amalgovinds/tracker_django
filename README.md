# Goal: A Routine Tracker and Glorified TODO App

## Learn some infra along the way

# TODO
1. Implement Nested Routing in Django
2. Improve Serializers(DRY)
3. Delpoyment Pipeline 

# Notes

## Nested Serializers
- Nested Serializers are good for a Read-Only Scenario, Create can also be managed, Update complications things. The approach to make data persist while patching new data results in a complex logic which needs to configuration according to the model relationships. Otherwise dump the data and create new related objects each time. *OUCH*
- So read using Nested and write using Flat serializers.
