from rest_framework         import serializers
from ch1.models             import TestCases, StringInputs



class StringInputsSerializer(serializers.ModelSerializer):
    class Meta:
        model   = StringInputs
        fields  = ['string_input']

class TestCasesSerializer(serializers.ModelSerializer):
    # regex  = serializers.SlugRelatedField(many=True, read_only=True, slug_field='string_input')
    # strings  = StringInputsSerializer(many=True)
    class Meta:
        model   = TestCases
        fields  = ['id', 'regex']
        # fields  = ['id', 'regex', 'strings']

    # def create(self, validated_data):
    #     strings_data    = validated_data.pop('string')
    #     test_case       = TestCases.objects.create(**validated_data)
    #     for string in strings_data:
    #         StringInputs.objects.create(test_case=test_case, **string)
    #     return test_case
    #
