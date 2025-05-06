print("Loading custom_policies module")

from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.core.policies.policy import Policy
from rasa.shared.core.trackers import DialogueStateTracker
from rasa.shared.core.domain import Domain
from typing import List, Text, Dict, Any

print("Imports successful")

@DefaultV1Recipe.register(
    [DefaultV1Recipe.ComponentType.POLICY_WITHOUT_END_TO_END_SUPPORT],
    is_trainable=True,
)
class FallbackPolicy(Policy):
    def __init__(self, config: Dict[Text, Any], **kwargs) -> None:
        super().__init__(config, **kwargs)
        print("Custom FallbackPolicy loaded!")

    def train(
        self,
        training_trackers: List[DialogueStateTracker],
        domain: Domain,
        **kwargs,
    ) -> None:
        # Implement your training logic here
        pass

    def predict_action_probabilities(
        self,
        tracker: DialogueStateTracker,
        domain: Domain,
        **kwargs,
    ) -> List[float]:
        # Implement your prediction logic here
        return [0.0] * domain.num_actions