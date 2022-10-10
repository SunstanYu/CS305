import dns.resolver

domain_name = "www.163.com"

a = dns.resolver.resolve(domain_name, 'A', raise_on_no_answer=False)
aaaa = dns.resolver.resolve(domain_name, 'AAAA', raise_on_no_answer=False)
ns = dns.resolver.resolve(domain_name, 'NS', raise_on_no_answer=False)
mx = dns.resolver.resolve(domain_name, 'MX', raise_on_no_answer=False)
cname = dns.resolver.resolve(domain_name, 'CNAME', raise_on_no_answer=False)

types = [a, aaaa, ns, mx, cname]

for t in types:
    print()
    if len(t.response.answer) <= 1:
        print(f"Query type {str(t.rdtype)[10:]} does not exist")
    else:
        print(f"Query type: {str(t.rdtype)[10:]}")
        for i in t.response.answer:
            for j in i.items:
                print(j)
