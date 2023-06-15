import { createClient } from '@sanity/client'
const client = createClient({
    projectId: 'bnpx4knh',
    apiVersion: '2023-06-15',
    dataset: 'production',
    token: 'skNP4wJzEwq2kDBcybVZdLGDA03R9AZ1ISXDtgVFcHDi2NkMdubu8WUdRkxa9WUWnQFRK3ocGqIFPQyaelUk8fJnYrKAkMNuT3oSw5cxMVKVTQHLaEHg9P3Ot7ibhaeViNvYDsWXmU10gmPzPmrhJz7rHZsD915PiJqnNcN4gMqftAo6i85V',
    useCdn: false
})

client.create({
    _type: 'post',
    title: 'My first post',
    body: [
        {
            _type: 'block',
            style: 'normal',
            markDefs: [],
            children: [
                {
                    _type: 'span',
                    text: 'Hello world!'
                }
            ]
        }
    ]
})
.then(res => {
    console.log(`document was created, document ID is ${res._id}`)
}).catch(err => {
    console.error('Oh no, the update failed: ', err.message)
})