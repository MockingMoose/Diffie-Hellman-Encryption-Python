from main import generate_shared_key, generate_public_key,pubBase, aliceKey, bobKey
import pytest, random
primesList = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


@pytest.mark.parametrize("run_number", [1, 2, 3, 4, 5])
def test_generate_shared_key(run_number):
    pubPrime = random.choice(primesList)
    bobPubTest = generate_public_key(pubBase, pubPrime, bobKey)
    alicePubTest = generate_public_key(pubBase, pubPrime, aliceKey)

    aliceSharedTest = generate_shared_key(bobPubTest, pubPrime, aliceKey)
    bobSharedTest = generate_shared_key(alicePubTest, pubPrime, bobKey)
    print(f"\n{run_number}: Alice Shared: {aliceSharedTest} | Bob Shared: {bobSharedTest}")
    assert aliceSharedTest == bobSharedTest