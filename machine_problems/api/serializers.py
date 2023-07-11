from rest_framework         import serializers
from ch1.models             import TestCases, StringInputs



class StringInputsSerializer(serializers.ModelSerializer):
    class Meta:
        model   = StringInputs
        fields  = ['string_input']

class TestCasesSerializer(serializers.ModelSerializer):
    strings  = StringInputsSerializer(many=True)
    class Meta:
        model   = TestCases
        fields  = ['id', 'regex', 'strings']

    def create(self, validated_data):
        strings_data    = validated_data.pop('strings')
        case            = TestCases.objects.create(**validated_data)
        for string in strings_data:
            StringInputs.objects.create(case=case, **string)
        return case

    def update(self, instance, validated_data):
        strings_data    = validated_data.pop('strings')
        instance.regex  = validated_data.get('regex', instance.regex)
        instance.save()

        existing_string_inputs      = instance.strings.all()
        existing_string_inputs_ids  = [str(input.id) for input in existing_string_inputs]

        for string_data in strings_data:
            string_id = string_data.get('id', None)
            if string_id in existing_string_inputs_ids:
                string_input                = existing_string_inputs.get(id=string_id)
                string_input.string_input   = string_data.get('string_input', string_input.string_input)
                string_input.save()
            else:
                StringInputs.objects.create(case=instance, **string_data)

        return instance
